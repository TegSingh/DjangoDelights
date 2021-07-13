from django import forms
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase

class IngredientCreateForm(forms.ModelForm):
    class Meta: 
        model = Ingredient
        fields = ("name", "quantity", "unit", "unit_price")    

class MenuItemCreateForm(forms.ModelForm):
    class Meta: 
        model = MenuItem
        fields = ("title", "price")