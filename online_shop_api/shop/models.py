from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)
    
    
    def __str__(self):
        return self.name
    

class Products(models.Model):
    image = models.ImageField(upload_to="products")
    name = models.CharField(max_length=100)
    amount_db = models.BigIntegerField(default=0)
    price = models.FloatField(default=0)
    description = models.TextField(null=True)
    
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
    
    
class Wishlist(models.Model):
    session_key = models.CharField(max_length=250)
    products = models.ManyToManyField(Products,related_name='products', blank=True)
    
    
    def __str__(self):
        return self.session_key


class CartItems(models.Model):
    session_key = models.CharField(max_length=250)
    quantity = models.IntegerField(default=0)
    product = models.OneToOneField(Products,on_delete=models.CASCADE, blank=True)
    
    
    def __str__(self):
        return self.session_key