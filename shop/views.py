from django.shortcuts import get_object_or_404 
from django.views.generic import TemplateView,ListView,DetailView
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin


class ShopPage(ListView):
    model = Product
    template_name = "shop/shop.html"
    context_object_name = 'product_list'

    def get_queryset(self):
        category_name = self.kwargs.get('category')
        if category_name:
            category = get_object_or_404(Category, name=category_name)
            return Product.objects.filter(category=category)
        else:
            return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context

class ProductDetails(DetailView):
    model = Product
    template_name = 'shop/product-details.html'
    context_object_name = 'product'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ctg = self.object.category
        context['related_products'] = Product.objects.filter(category=ctg)
        return context

class WishistPage(LoginRequiredMixin,TemplateView):
    template_name = "shop/wishlist.html"
