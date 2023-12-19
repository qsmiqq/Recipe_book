from django import forms
from .models import Recipe


class AddRecipe(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'cooking_time', 'cooking_method', 'complexity']
