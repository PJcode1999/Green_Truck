from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View,ListView,CreateView,TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import *
from .models import *

# Create your views here.
    
class AddToCartView(SuccessMessageMixin,LoginRequiredMixin,View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        user=request.user
        cart, created = Cart.objects.get_or_create(user=user, ordered=False)
        cart_item, item_created = CartItems.objects.get_or_create(
            cart=cart,
            user=user,
            product=product,
        )
        if not item_created:
            cart_item.quantity += 1
            cart_item.save()
        return redirect(request.META.get('HTTP_REFERER'))

class RemoveFromCartView(LoginRequiredMixin, ListView):
    def get(self, request, cart_item_id):
        cart_item = get_object_or_404(CartItems,id=cart_item_id, user=request.user)
        if cart_item:
            cart_item.delete()
        return redirect('cart:cart')
    

class DecreaseQuantityView(LoginRequiredMixin, View):
    def get(self, request, cart_item_id):
        cart_item = get_object_or_404(CartItems, id=cart_item_id, user=request.user)        
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()        
        return redirect('cart:cart')


class CartListView(LoginRequiredMixin, ListView):
    model = CartItems
    template_name = 'cart/cart.html'  
    context_object_name = 'products'

    def get_queryset(self):
        return CartItems.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_items = self.get_queryset()

        subtotal = sum(item.price for item in cart_items)
        total_discount = sum(item.product.discount for item in cart_items)

        if subtotal <=500:
            delivery_charges = 20.00  
        else:
            delivery_charges = 0.00 

        total_bill = (subtotal + delivery_charges) - total_discount

        context['subtotal'] = subtotal
        context['delivery_charges'] = delivery_charges
        context['total_bill'] = total_bill
        context['total_discount'] = total_discount

        return context


class AddressCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = ShippingAddress
    form_class = ShippingAddressForm
    success_url = reverse_lazy('cart:checkout')
    template_name = "cart/checkout.html"
    success_message = "Address save successfully"
    context_object_name = 'form'

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)