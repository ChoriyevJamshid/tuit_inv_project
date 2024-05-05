
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('store:product_list_by_category',
                       args=[self.slug])

    def __str__(self):
        return self.title


class Product(models.Model):
    class ProductType(models.TextChoices):
        NEWSPAPER = 'Newspaper'
        JOURNAL = 'Journal'

    product_type = models.CharField(max_length=100, choices=ProductType.choices)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.CharField(max_length=100)
    description = models.TextField()

    image = models.ImageField(upload_to='products')
    price = models.DecimalField(max_digits=5, decimal_places=2)

    date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    objects = models.Manager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('store:product_detail',
                       args=[self.id, self.slug])

