from django import template
from django.db.models import Sum
from django.contrib.auth import get_user_model

from ..models import Cart

User = get_user_model()

register = template.Library()


@register.simple_tag
def get_total_price(user):
    total_price = 0
    if isinstance(user, User):
        total_price = Cart.objects.filter(user=user).aggregate(total=Sum('price'))['total']
    if total_price is None:
        total_price = 0
    total_price = f'{total_price}.00'
    return total_price
