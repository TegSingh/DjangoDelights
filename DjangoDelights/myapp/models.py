from django.db import models


# Create your models here.
class Ingredient(models.Model):
    # Properties of the ingredient method
    name = models.TextField(max_length=30)
    quantity = models.FloatField(default=0.0)
    unit = models.TextField(max_length=10)
    unit_price = models.FloatField(default=0.0)

    # Overwrite the str method
    def __str__(self):
        return self.quantity + self.unit + "[" + self.unit_price + "per unit] of " + self.name 
    
class MenuItem(models.Model):
    # Each Item in the Menu has a title and price
    title = models.TextField(max_length=30)
    price = models.FloatField(default=0.0)

# This models defines what quantity of an ingredient is a requirement for a particular menu item 
class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.DO_NOTHING) # on_delete = models.CASCADE means if a reciperequirement was deleted, the referenced menu_item will be deleted too 
    ingredient = models.ForeignKey(Ingredient, on_delete=models.DO_NOTHING)
    quantity = models.FloatField(default=0.0)

    # Overwrite the predefined str method of the class
    def __str__(self):
        return self.quantity + " units of " + self.ingredient + " used in " + self.menu_item 

    # Function to calculate revenue per item purchased[Can be used to calculate total revenue per purchase] (in progress..)
    def calculateRevenue(self):
        return self.menu_item.price - (self.ingredient.quantity * self.ingredient.unit_price) 

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.DO_NOTHING)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.menu_item + " purchased at " + self.timestamp
