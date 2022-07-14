from django.shortcuts import render
from django.views.generic import View,ListView,DetailView,CreateView,TemplateView
from shop.models import *
from .models import *
# Create your views here.
class HomePage(TemplateView):
    template_name = "main/home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_cat'] = ProductCategory.objects.all()
        return context
    
class PageView(DetailView):
    template_name = 'main/about.html'
    model = Page