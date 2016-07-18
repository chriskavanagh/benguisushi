from django import template
from django.db.models import Count

register = template.Library()

@register.simple_tag
def empty_cart_message():
    return("Cart Is Empty")
    