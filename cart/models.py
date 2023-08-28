from django.db import models
from django.contrib.auth.models import User
from shop.models import Product
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
# Create your models here.


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    total_price = models.FloatField(default=0.00)

    def __str__(self):
        return str(self.user.username) + " / "+str(self.total_price)


class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(default=0.00)
    quantity = models.PositiveIntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)+" / "+str(self.product.name)


@receiver(pre_save, sender=CartItems)
def correct_price(sender, **kwargs):
    cart_items = kwargs['instance']
    price_of_product = Product.objects.get(id=cart_items.product.id)
    cart_items.price = cart_items.quantity * float(price_of_product.price)
    
    cart = Cart.objects.get(id=cart_items.cart.id)
    cart.total_price = cart_items.price
    cart.save()


STATES_CHOICES = [
    ("SELECT STATE","Select State"),
    ("ANDHRA PRADESH","Andhra Pradesh"),
    ("ARUNACHAL PRADESH","Arunachal Pradesh"),
    ("ASSAM","Assam"),
    ("BIHAR","Bihar"),
    ("CHHATTISGARH","Chhattisgarh"),
    ("GOA","Goa"),
    ("GUJARAT","Gujarat"),
    ("HARYANA","Haryana"),
    ("HIMACHAL","Himachal"),
    ("PRADESH","Pradesh"),
    ("JHARKHAND ","Jharkhand "),
    ("KARNATAKA ","Karnataka "),
    ("KERALA","Kerala"),
    ("MAHARASHTRA ","Maharashtra "),
    ("MANIPUR ","Manipur "),
    ("MEGHALAYA","Meghalaya"),
    ("MIZORAM","Mizoram"),
    ("NAGALAND","Nagaland"),
    ("ODISHA","Odisha"),
    ("PUNJAB","Punjab"),
    ("RAJASTHAN","Rajasthan"),
    ("SIKKIM","Sikkim"),
    ("TAMIL NADU","Tamil Nadu"),
    ("TELANGANA","Telangana"),
    ("TRIPURA","Tripura"),
    ("UTTARAKHAND","Uttarakhand"),
    ("UTTAR PRADESH","Uttar Pradesh"),
    ("WEST BENGAL","West Bengal"),
]

class ShippingAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    state = models.CharField(max_length=50,choices=STATES_CHOICES,default=True)
    address_1 = models.TextField(max_length=100)
    address_2 = models.TextField(max_length=100,blank=True)
    city = models.CharField(max_length=50)
    postpin = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    
    def __str__(self):
        return str(self.user.username)+" / "+str(self.id)
