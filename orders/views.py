from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from store.models import Product
from .models import Cart, OrderItem
from .forms import CartAddProductForm, OrderCreateForm


@login_required
def cart_list(request):
    carts = Cart.objects.filter(user=request.user)
    form = CartAddProductForm()
    context = {
        'carts': carts,
        'form': form
    }

    return render(request,
                  'orders/cart/list.html',
                  context)


@require_POST
def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart = Cart.objects.filter(user=request.user, product=product)
        if cart.exists():
            cart = cart.first()
            cart.duration = cd['duration']
        else:
            cart = Cart(
                user=request.user,
                product=product,
                duration=cd['duration'],
            )
        cart.save()
        messages.success(request, 'Your cart has been added.')
    else:
        messages.error(request, "Invalid cart")
    return redirect('orders:cart_list')


@require_POST
def cart_remove(request, cart_id):
    cart = get_object_or_404(Cart, user=request.user, id=cart_id)
    cart.delete()
    messages.success(request, f'Your cart has been removed.')
    return redirect('orders:cart_list')


@login_required
def order_create(request):
    carts = request.user.carts.all()
    if request.method == 'POST':

        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for cart in carts:
                OrderItem.objects.create(
                    order=order,
                    product=cart.product,
                    price=cart.price,
                    duration=cart.duration,
                )
            messages.success(request, "Your order has been success")
            carts.delete()
            return redirect('payment:process')
        else:
            messages.error(request, "Something wrong with our informations!")
            return redirect('order:cart_list')
    else:
        form = OrderCreateForm()

    return render(request,
                  template_name='orders/order/create.html',
                  context={
                      'form': form,
                      'carts': carts
                  })







