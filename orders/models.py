from django.db import models
from django.contrib.auth import get_user_model
from store.models import Product

User = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='carts')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='carts')
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                default=0)
    duration = models.PositiveSmallIntegerField(default=1)

    objects = models.Manager()

    def __str__(self):
        return f'{self.user} {self.product}'

    def save(self, *args, **kwargs):
        if self.price == 0:
            self.price = self.product.price * self.duration

        super().save(*args, **kwargs)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='orders')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.__class__.__name__}: {self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name="order_items")
    price = models.DecimalField(max_digits=10, decimal_places=2)

    duration = models.PositiveSmallIntegerField(default=1)

    objects = models.Manager()

    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        return self.price * self.duration


















