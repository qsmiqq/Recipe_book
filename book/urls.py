from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecipesListView.as_view(), name='recipes'),
    path('add_recipe', views.add_recipe, name='add_recipe'),
    path('<slug:recipe_slug>', views.recipe_info, name='recipe_info'),
    path('edit/<int:recipe_id>', views.edit_recipe, name='edit_recipe'),
    path('delete/<int:get_recipe>', views.recipe_delete, name='delete_recipe')
    ]
