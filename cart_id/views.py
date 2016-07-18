from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from cart_id.forms import ProductAddToCartForm
from .models import CartItem

from products.models import Product
from django.views.decorators.http import require_POST

from cart_id.forms import ProductAddToCartForm
from products.models import Product

from ecommerce import settings
import random, string
from decimal import Decimal


#http://pasteboard.co/1fNvc0YU.png  screen shot
#http://pasteboard.co/1KtIgmoY.png



# Create your views here.

## could possibly use hashlib to create random cart_id (see below).
def _cart_id(request):
    '''gets cart_id from session or creates cart_id.'''
    cart_id = request.session.get(settings.CART_SESSION_ID)
    if not cart_id:
        cart_id = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(50)])
        request.session[settings.CART_SESSION_ID] = cart_id
    return cart_id
    
    
def show_cart(request):
    '''shows the cart with all products and form.'''
    cart_id = _cart_id(request)
    cart_items = CartItem.objects.filter(cart_id=cart_id)
    objects = []
    form = None
    for item in cart_items:
        q = item.quantity
        add_product_form = ProductAddToCartForm(initial={'quantity': q})
        objects.append({'item':item, 'form': add_product_form})
    context = {'objects': objects}
    #print context
    return render(request, 'cart_id/cart.html', context)
    
    
def update_cart(request):
    '''updates quantity of item/product in cart.'''
    cart_id = _cart_id(request)
    quantity = request.POST['quantity']
    item_pk = request.POST['item_pk']
    cart_item = get_object_or_404(CartItem, pk=item_pk, cart_id=cart_id)
    if cart_item:
        cart_item.quantity = quantity
        cart_item.save()
        return redirect('cart:show_cart')
    
   
def cart_add(request, product_slug):
    '''adds product to cart or updates quantity'''
    cart_id = _cart_id(request)
    p = get_object_or_404(Product, slug=product_slug)
    cart_products = CartItem.objects.filter(cart_id=cart_id)
    product_in_cart = False
    if request.method == 'POST':        
        form = ProductAddToCartForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            quantity = cd['quantity']
            update = cd['update']
            for cart_item in cart_products:
                if cart_item.product.id == p.id:
                    cart_item.quantity = quantity    
                    cart_item.save()
                    product_in_cart = True
            if not product_in_cart:
                ci = CartItem()
                ci.product = p
                ci.update_quantity(quantity)
                #ci.quantity += quantity    
                ci.cart_id = cart_id
                ci.save()
            return redirect('cart:show_cart')
    else:
        return render(request, 'products/single.html', {})
        

def get_cart_items(request):
    '''returns all items in cart.'''
    return CartItem.objects.filter(cart_id=_cart_id(request))
    
      
def cart_count(request):
    '''count of cart items in cart.'''
    cart_items = CartItem.objects.filter(cart_id=_cart_id(request))
    return cart_items.count()
    
    
def remove(request, pk):
    '''removes item/product from cart.'''
    cart_id = _cart_id(request)
    cart_item = get_object_or_404(CartItem, pk=pk, cart_id=cart_id)
    if cart_item:
        cart_item.delete()
        return redirect('cart:show_cart')
        
        
def item_subtotal(request):
    '''gets item/product total.'''
    cart_total = Decimal('0.00')
    cart_id = _cart_id(request)
    cart_products = CartItem.objects.filter(cart_id=cart_id(request))
    for cart_item in cart_products:
        cart_total += cart_item.product.price * cart_item.quantity
    return cart_total
        
        
def cart_empty(request):
    '''empties cart.'''
    cart_id = _cart_id(request)
    user_cart = CartItem.objects.filter(cart_id=_cart_id(request))
    user_cart.delete()
    
    
def is_empty(request):
    '''boolean to check if cart is empty.'''
    return cart_count(request) == 0
        
        
        
        
# import hashlib, random
# cart_id = hashlib.sha1(str(random.random())).hexdigest()