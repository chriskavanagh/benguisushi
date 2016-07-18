#import json
#from json import dumps
from ecommerce import settings
from django.shortcuts import render
#from cart_id.models import CartItem
from products.models import Product
#from django.core import serializers
from django.http import Http404, HttpResponse


# Create your views here.    
    
def home(request):
    return render(request, 'home.html', {})
    
    
def search(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')
        products = Product.objects.filter(title__contains=query)
        context = {'products': products}
        return render(request, 'search.html', context)
        
        
        
        
# def _cart_id(request):
    # '''gets cart_id from session or creates cart_id.'''
    # cart_id = request.session.get(settings.CART_SESSION_ID)
    # if not cart_id:
        # cart_id = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(50)])
        # request.session[settings.CART_SESSION_ID] = cart_id
    # return cart_id
    
    
    
# def dialog(request):
#''' https://collincode.wordpress.com/2014/09/24/jquery-ui-popup-with-django-backend/ '''
    # return render(request, 'dialog.html', {})
    
    
# def my_cart(request):
    # # '''ajax request to show cart items on hover.'''
    # if request.is_ajax():        
        # cart_id = _cart_id(request)
        # cart_items = CartItem.objects.filter(cart_id=cart_id)
        # context = {'cart_items': cart_items}
        # return render(request, 'my_cart.html', context)
    # else:
        # raise Http404
        
    
# converting obj to json  
# def my_cart(request):
    # '''ajax request to show cart items on hover.'''
    # if request.is_ajax():        
        # cart_id = _cart_id(request)
        # cart_items = CartItem.objects.filter(cart_id=cart_id)
        # #data = list(CartItem.objects.filter(cart_id=cart_id).values('product'))
        # return HttpResponse(json.dumps([str(obj.product.title) for obj in cart_items]), content_type='application/json')
    # else:
        # raise Http404
        
        
