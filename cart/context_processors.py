from cart.models import CartItems  

def cart_item_count(request):
    if request.user.is_authenticated:
        cart_items = CartItems.objects.filter(user=request.user)
        return {'cart_item_count': cart_items.count()}
    return {'cart_item_count': 0}
