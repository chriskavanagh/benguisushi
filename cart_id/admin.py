from django.contrib import admin
from .models import CartItem

# Register your models here.
class CartItemAdmin(admin.ModelAdmin):
    #date_hierarchy = 'date_added'
    list_display = ['cart_id', 'date_added', 'quantity', 'product']
    
    class Meta:
        model = CartItem
        
admin.site.register(CartItem, CartItemAdmin)