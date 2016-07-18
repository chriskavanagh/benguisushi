from cart_id.models import CartItem
from cart_id.views import _cart_id
from decimal import Decimal


def cart_count(request):
    cart_items = CartItem.objects.filter(cart_id=_cart_id(request))
    return {'cart_items_count': cart_items.count()}
    
    
def cart_total_cost(request):
    '''gets carts total cost.'''
    cart_id = _cart_id(request)
    cart_items = CartItem.objects.filter(cart_id=cart_id)
    cart_total = sum(Decimal(item.product.price) * item.quantity for item in cart_items)
    return {'cart_total': cart_total}
    
    
def cart_items_context(request):
    cart_id = _cart_id(request)
    cart_items = CartItem.objects.filter(cart_id=cart_id)
    return {'cart_items': cart_items}
    