from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('ingredient/', views.IngredientsList.as_view(), name="ingredient"),
    path('finances/', views.finances, name="finances"),
    path('purchase/', views.PurchaseList.as_view(), name="purchase"),
]
