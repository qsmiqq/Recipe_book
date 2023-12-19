from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView
from .models import Recipe, Ingredients
from django.http import HttpResponseNotFound, HttpResponseRedirect
from .forms import AddRecipe


def home(request):
    return render(request, 'home.html')


class RecipesListView(ListView):
    model = Recipe
    template_name = "recipes.html"
    context_object_name = "recipes"

    def get_queryset(self):
        return Recipe.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def recipe_info(request, recipe_slug):
    recipe = Recipe.objects.prefetch_related(recipe_slug)
    ingredients = recipe.ingredients
    context = {
        'recipe': recipe,
        'ingredients': ingredients,
    }
    return render(request, 'recipes_info.html', context=context)


def add_recipe(request):
    form = AddRecipe()
    if request.method == "POST":
        form = AddRecipe(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('recipes')
    context = {
        'form': form
    }
    return render(request, 'recipes_add.html', context=context)


def edit_recipe(request, recipe_id):
    form = Recipe.objects.get(id=recipe_id)
    form_ = AddRecipe(request.POST, instance=form)
    if request.method == "POST":
        if form_.is_valid():
            obj = form_.save(commit=False)
            obj.creator = request.user
            obj.save()
            form_.save_m2m()
            return redirect('recipes')
    context = {
        'form': form_
    }
    return render(request, "recipes_edit.html", context=context)



def recipe_delete(request, get_recipe):
    recipe = Recipe.objects.get(id=get_recipe)
    recipe.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
