from rest_framework import serializers

from .models import Category, Products, Wishlist, CartItems


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"



class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=True)
    
    class Meta:
        model = Products
        fields = "__all__"
        

class WishlistSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, required=True)
    
    class Meta:
        model = Wishlist
        fields = '__all__'
        

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(required=True)
    
    
    class Meta:
        model = CartItems
        fields = '__all__'
        