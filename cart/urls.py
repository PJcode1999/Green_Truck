from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.CartListView.as_view(), name='cart'),
    path('checkout/', views.AddressCreateView.as_view(), name='checkout'),
    path('add/<int:product_id>/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('decrease/<int:cart_item_id>/', views.DecreaseQuantityView.as_view(), name='decrease_quantity'),
    path('remove/<int:cart_item_id>/', views.RemoveFromCartView.as_view(), name='remove_from_cart'),
]
