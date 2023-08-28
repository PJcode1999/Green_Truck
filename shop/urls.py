from django.urls import path 
from . import views
urlpatterns = [
    path('', views.ShopPage.as_view(), name='shop'),
    path('shop/<pk>', views.ProductDetails.as_view(), name='product-details'),
    path('<str:category>', views.ShopPage.as_view(), name='shop-category'),
    path('wishlist/', views.WishistPage.as_view(), name='wishlist'),
]