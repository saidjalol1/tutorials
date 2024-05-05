from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Models & serializers
from .models import Products, CartItems, Category, Wishlist
from .serializers import (  ProductSerializer,CartItemSerializer, 
                            CategorySerializer, WishlistSerializer)

# Views

class HomeView(APIView):
    def get(self,request):
        session_key = request.session.session_key
        print(session_key)
        if not session_key:
            request.session.save()
            session_key = request.session.session_key
        print(session_key)
        
        products = Products.objects.all()
        category = Category.objects.all()
        data = {"products" : ProductSerializer(products, many=True).data,"categories": CategorySerializer(category, many=True).data}
        return Response(data)


class ProductDetailView(APIView):
    def get(self, request, pk):
        product =  get_object_or_404(Products, id=pk)
        data = ProductSerializer(product).data
        return Response(data)


class CartView(APIView):
    pass


class WishlistView(APIView):
    pass