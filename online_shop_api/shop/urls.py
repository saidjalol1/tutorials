from django.urls import path
from .views import HomeView, CartView, WishlistView,ProductDetailView
app_name = 'shop'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('cart/', CartView.as_view(), name='cart'),
    
    path('product/<int:pk>', ProductDetailView.as_view(), name='detail'),
]
