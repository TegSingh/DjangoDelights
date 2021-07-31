from django.urls import path
from . import views

# NOTE: This redirects to views not to templates
urlpatterns = [
    path('', views.home, name='home'),
    path('ingredient/', views.IngredientsList.as_view(), name='ingredient'),
    path('finances/', views.finances, name='finances'),
    path('purchase/', views.PurchaseList.as_view(), name='purchase'),
    path("menuitem/create", views.MenuItemCreate, name="menuitem_create"),
    path("menuitem/update/<int:pk>", views.MenuItemUpdate, name="menuitem_update"), 
    path("menuitem/delete/<int:pk>", views.MenuItemDelete, name="menuitem_delete"), 
    path("ingredient/create", views.IngredientsCreate, name="ingredient_create"),
    path("ingredient/update/<int:pk>", views.IngredientsUpdate, name="ingredient_update"), 
    path("ingredient/delete/<int:pk>", views.IngredientsDelete, name="ingredient_delete"), 
]
