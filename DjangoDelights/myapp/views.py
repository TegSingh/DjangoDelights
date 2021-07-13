from django.shortcuts import render, redirect
from .models import Ingredient, RecipeRequirement, MenuItem, Purchase
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import Http404
from .forms import IngredientCreateForm, MenuItemCreateForm

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
    model = Ingredient
    template_name = 'myapp/ingredients.html'

    def get_queryset(self):
        return Ingredient.objects.all()
    
# A view to add Ingredient in the inventory
class IngredientsCreate(CreateView):
    model = Ingredient

# A view to update Ingredient parameters in inventory
class IngredientUpdate(UpdateView): 
    model = Ingredient

# A view to delete ingredients
class IngredientsDelete(DeleteView):
    model = Ingredient

# View to add Menu Items to the inventory
def MenuItemCreate(request):
    # Check if the submitted form method was POST
    if request.method == 'POST':
        newitem = MenuItem()
        newitem.title = request.POST['title']
        newitem.price = request.POST['price']
        # Save the new item in the database
        newitem.save()

    # Render the form template
    return redirect('home')

# View to delete Menu Items
class MenuItemDelete(DeleteView):
    model = MenuItem

# View to update available Menu items
class MenuItemUpdate(UpdateView):
    model = MenuItem

# View the purchases made at the restaurant
class PurchaseList(ListView):
    model = Purchase
    template_name = 'myapp/purchase.html'

    def get_queryset(self):
        return Purchase.objects.all()
    
# View to add Purchase
class PurchaseCreate(CreateView):
    model = Purchase

# View the profit and revenue for the restaurant [make this function based]
def finances(request):
    # Calculate Revenue and Profit
    revenue = 0
    purchase = Purchase.objects.all()
    for item in purchase: 
        revenue += item.menu_item.price
    context = {
        "revenue": revenue
    }
    return render(request, 'myapp/finances.html', context)
    