import stripe
from .forms import StripeForm
from ecommerce import settings
from .models import OrderItem, Order
from forms import OrderCreateForm
from cart_id.models import CartItem
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import Http404
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from cart_id.views import show_cart

#from cart_id import views as cart
#from decimal import Decimal

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.
def _cart_id(request):
    '''gets cart_id from session or creates cart_id.'''
    cart_id = request.session.get(settings.CART_SESSION_ID)
    if not cart_id:
        cart_id = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(50)])
        request.session[settings.CART_SESSION_ID] = cart_id
    return cart_id
    
    
def order_create(request):
    '''create a cust order.'''
    cart_id = _cart_id(request)
    cart_items = CartItem.objects.filter(cart_id=cart_id)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart_items:
                OrderItem.objects.create(order=order,
                                         product=item.product,
                                         price=item.product.price,
                                         quantity=item.quantity)
            request.session['order_id'] = order.id
            return redirect('orders:checkout')

    else:
        form = OrderCreateForm()
    context = {'cart_items': cart_items, 'form': form}
    return render(request, 'orders/create.html', context)
    
    
def checkout(request):
    '''check customer out/pay bill.'''
    cart_id = _cart_id(request)                              # cart_items now a context_processor, no need for this line.
    cart_items = CartItem.objects.filter(cart_id=cart_id)    # cart_items now a context_processor, no need for this line.
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    order_amount = order.get_total_cost
    stripe_amount = int(order_amount * 100)
    print order_amount
    publishable_key = settings.STRIPE_PUBLISHABLE_KEY
    if request.method == "POST":
        #stripe.api_key = settings.STRIPE_SECRET_KEY
        token = request.POST.get('stripeToken')
        print token
        customer = stripe.Customer.create(description='test', source=token)
        charge = stripe.Charge.create(amount=stripe_amount, currency='usd', customer=customer)
        print charge
        if charge['captured']:
            order.paid = True      # change order.paid to True.
            order.save()           # save it.
            cart_items.delete()    # clear cart does NOT clear cart_id.
            return redirect('orders:thanks')        
    context = {'cart_items': cart_items, 'stripe_amount': stripe_amount, 'publishable_key': publishable_key}
    return render(request, 'orders/checkout.html', context)
    
    
def thanks(request):
    return render(request, 'orders/thanks.html', {})
    
    
def test(request):
    return render(request, 'orders/test.html', {})
    
    
    
    
    
## copy of current checkout view.
    
# def checkout(request):
    # order_id = request.session.get('order_id')
    # order = get_object_or_404(Order, id=order_id)
    # order_amount = order.get_total_cost
    # print order_amount
    # publishable_key = settings.STRIPE_PUBLISHABLE_KEY
    # if request.method == "POST":
        # stripe.api_key = settings.STRIPE_SECRET_KEY
        # token = request.POST.get('stripeToken')
        # # # #token = request.POST['stripeToken']
        # print token
        # customer = stripe.Customer.create(description='test', source=token)
        # print customer
        # #stripe.Charge.create(amount=500, currency='usd', source=token, description='test')
        # stripe.Charge.create(amount=order_amount, currency='usd', customer=customer)
        # return redirect('orders:thanks')        
    # context = {'order_amount': order_amount, 'publishable_key': publishable_key}
    # return render(request, 'orders/checkout.html', context)
    
    
