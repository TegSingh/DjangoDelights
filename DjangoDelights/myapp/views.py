from django.shortcuts import render
from .models import Ingredient, RecipeRequirement, MenuItem, Purchase
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import Http404

# Create your views here.

# Home view to display the menu when the website opens
def home(request): 
    # Check if menu has items
    try: 
        menu = MenuItem.objects.all()
    except Menuitem.DoesNotExist:
        raise Http404()

    context =  {"menu": menu}
    # render (request name, template name, object to be passed to template)
    return render(request, 'myapp/home.html', context)


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
def finances(request):
    # Calculate Profit and Revenue 
    pass