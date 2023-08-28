from django.views.generic import TemplateView,ListView 
from django.shortcuts import get_object_or_404
from shop.models import *

class HomePage(ListView):
    model = Product
    template_name = "home.html"
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

