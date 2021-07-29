from django import forms
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase 

class MenuItemUpdateForm(forms.ModelForm):
    class Meta: 
        model = MenuItem
        fields = '__all__'