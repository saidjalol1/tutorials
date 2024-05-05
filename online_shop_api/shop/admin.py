from django.contrib import admin

from .models import Products, Category, CartItems, Wishlist

admin.site.register(Products)
admin.site.register(CartItems)
admin.site.register(Wishlist)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("name",)}
