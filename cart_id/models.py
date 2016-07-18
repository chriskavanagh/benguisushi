from __future__ import unicode_literals
from django.db import models
from products.models import Product

# Create your models here.
class CartItem(models.Model):
    cart_id = models.CharField(max_length=50, db_index=True)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    product = models.ForeignKey(Product)
    
    class Meta:
        ordering = ['date_added']
        
    @property
    def total(self):
        return self.quantity * self.product.price
        
    @property   
    def name(self):
        return self.product.title
        
    @property    
    def price(self):
        return self.product.price
        
    def update_quantity(self, quantity):
        self.quantity += int(quantity)
        self.save()
    
    def get_absolute_url(self):
        return self.product.get_absolute_url()