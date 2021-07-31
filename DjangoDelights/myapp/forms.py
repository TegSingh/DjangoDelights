from django import forms
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase 

class MenuItemUpdateForm(forms.ModelForm):
    class Meta: 
        model = MenuItem
        fields = '__all__'

class IngredientUpdateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'