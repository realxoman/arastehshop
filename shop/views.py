from django.shortcuts import render, redirect
from .models import *
from accounts.models import *
from django.views.generic import View,ListView,DetailView,CreateView,TemplateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.

class ProductCategoryListView(DetailView):
    model = ProductCategory
    template_name = "shop/category.html"

class ProductView(DetailView):
    model = Product
    template_name = "shop/product.html"
    
class CartView(LoginRequiredMixin, ListView):
    template_name = "shop/cart.html"
    model = Cart
    context_object_name= "objects"
    
    
    def get_queryset(self):
        return self.model.objects.filter(user=self.user)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user = None

    def dispatch(self, request, *args, **kwargs):
        self.user = request.user

        return super().dispatch(request, *args, **kwargs)

def cart_add_view(request):
    size = request.POST.get("size")
    product_id = request.POST.get("product_id")
    pro= Product.objects.get(id=product_id)
    print(request.user)
    myuser=request.user
    mysize= Size.objects.get(size_name=size)
    add_to_cart = Cart(product=pro,user=myuser,size=mysize).save()
    return redirect('shop:cart')
            
        
class DeleteCart(LoginRequiredMixin,DeleteView):
    model=Cart
    success_url = reverse_lazy('main:HomePage')
    
    
class CheckoutView(TemplateView):
    template_name = "shop/checkout.html"