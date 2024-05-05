from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from .models import Product, Category
from orders.forms import CartAddProductForm


def home(request):
    return render(request, 'home.html')


def product_list(request: HttpRequest, category_slug=None):
    category = None
    product_type = None
    categories = Category.objects.all()
    products = Product.objects.filter(is_active=True)

    print('\n\n')

    print('\n\n')

    if category_slug:
        if category_slug.title() in Product.ProductType.values:
            if category_slug.lower() == 'newspaper':
                products = products.filter(product_type=Product.ProductType.NEWSPAPER)
            else:
                products = products.filter(product_type=Product.ProductType.JOURNAL)
            product_type = category_slug
        else:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)

    return render(request,
                  'store/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'product_type': product_type})


@login_required
def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                is_active=True)
    form = CartAddProductForm()
    return render(request,
                  'store/product/detail.html',
                  {
                      'product': product,
                      'form': form,
                  })
