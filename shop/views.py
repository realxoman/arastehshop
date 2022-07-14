from django.shortcuts import render
from .models import *
from accounts.models import *
from django.views.generic import View,ListView,DetailView,CreateView,TemplateView
# Create your views here.

class ProductCategoryListView(ListView):
    model = Product
    template_name = "shop/category.html"

class ProductView(DetailView):
    model = Product
    template_name = "shop/product.html"
    
class CartView(TemplateView):
    template_name = "shop/cart.html"
    
class CheckoutView(TemplateView):
    template_name = "shop/checkout.html"