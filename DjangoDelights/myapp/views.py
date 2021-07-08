from django.shortcuts import render
from .models import Ingredient, RecipeRequirement, MenuItem, Purchase
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.

# A view to check all the ingredients in the inventory
class IngredientsList(ListView):
    Model = Ingredient

# A view to add Ingredient in the inventory
class IngredientsCreate(CreateView):
    Model = Ingredient

# A view to update Ingredient parameters in inventory
class IngredientUpdate(UpdateView): 
    Model = Ingredient

# A view to delete ingredients
class IngredientsDelete(DeleteView):
    Model = Ingredient

# View all items in the menu
class MenuList(ListView):
    Model = MenuItem

# View to add Menu Items to the inventory
class MenuCreate(CreateView):
    Model = MenuItem

# View to delete Menu Items
class MenuDelete(DeleteView):
    Model = MenuItem

# View to update available Menu items
class MenuUpdate(UpdateView):
    Model = MenuItem

# View the purchases made at the restaurant
class PurchaseList(ListView):
    Model = Purchase

# View to add Purchase
class PurchaseCreate(CreateView):
    Model = Purchase

# View the profit and revenue for the restaurant [make this function based]
def profitAndRevenue(request):
    # Calculate Profit and Revenue 