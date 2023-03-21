from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='ecomm-home'),
    path('shoppingcart/', views.shoppingcart, name = 'shopping-cart'),
    path('update_item/', views.updateItem, name='update_item' ),

]