from django.urls import path
from .views import *
app_name = 'shop'

urlpatterns = [
    path('cart/', CartView.as_view(), name="cart"),
    path('cart/delete/<int:pk>/', DeleteCart.as_view(), name="cart-delete"),
    path('cat/<str:slug>/', ProductCategoryListView.as_view(), name="product-list"),
    path('product/<str:slug>/', ProductView.as_view(), name='product')
]