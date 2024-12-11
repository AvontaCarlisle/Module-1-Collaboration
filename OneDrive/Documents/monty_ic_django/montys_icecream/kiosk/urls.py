from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('cones/', views.cones, name='cones'),
    path('cakes/', views.cakes, name='cakes'),
    path('milkshakes/', views.milkshakes, name='milkshakes'),
    path('froyo/', views.froyo, name='froyo'),
    path('sandwiches/', views.sandwiches, name='sandwiches'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
]
