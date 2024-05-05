from django.contrib import admin
from .models import Cart, OrderItem, Order


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'duration')


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    raw_id_fields = ('product', )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',
                    'email', 'address', 'city', 'state',
                    'postal_code', 'paid')

    list_filter = ('paid', 'created_at', 'updated_at')
    inlines = (OrderItemInline,)


