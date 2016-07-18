from django.shortcuts import render, get_object_or_404, redirect
from cart_id.forms import ProductAddToCartForm
from .models import Product
#from django.core.mail import send_mail


# Create your views here.
def product_list(request):
    '''view shows list of all active products'''
    products = Product.objects.all()
    context = {'products': products}
    print context
    return render(request, 'products/all.html', context)
    
    
def detail_view(request, slug):
    '''view shows individual product'''
    product = get_object_or_404(Product, slug=slug, active=True)
    form = ProductAddToCartForm(initial={'quantity': 1})
    context = {'product': product, 'form': form}
    print context
    return render(request, 'products/single.html', context)