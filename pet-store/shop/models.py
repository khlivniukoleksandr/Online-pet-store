from django.contrib.auth.models import AbstractUser
from django.db import models


class Customer(AbstractUser):
    phone_number = models.CharField(max_length=11, unique=True)
    address = models.TextField(blank=True)


class Category(models.Model):
    name = models.CharField(max_length=55)


class Product(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="product_images/", blank=True)
    stock = models.IntegerField(default=0)


class Cart(models.Model):
    user = models.OneToOneField(Customer, on_delete=models.CASCADE)
    address = models.TextField(blank=True)
    is_paid = models.BooleanField(default=False)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
