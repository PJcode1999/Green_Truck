from django.db import models

# Create your models here.

class Subscriber(models.Model):
    email = models.EmailField(max_length=200, unique=True)
    date = models.DateTimeField(auto_now_add=True) 
