from django.urls import path

from . import views

app_name = 'order'

urlpatterns = [
    path('cart/', views.cart_list, name='cart_list'),
    path('cart/add/<int:product_id>/', views.cart_add,
         name='cart_add'),
    path('cart/remove/<int:cart_id>/', views.cart_remove,
         name='cart_remove'),
    path('order/create/', views.order_create, name='order_create'),

]
