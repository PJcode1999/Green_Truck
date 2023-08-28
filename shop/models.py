from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    cat_photo = models.ImageField(upload_to='category')
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='products')
    price = models.IntegerField()
    discount = models.FloatField(default=10.15)
    quantity = models.CharField(max_length=20,default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    in_stock = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name