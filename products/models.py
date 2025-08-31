from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone  # Added for default datetime
from django.core.validators import MinValueValidator

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)  # Required
    description = models.TextField(blank=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=False,
        validators=[MinValueValidator(0.01)]  # Price > 0
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', default=1)
    stock_quantity = models.PositiveIntegerField(
        default=0, blank=False,
        validators=[MinValueValidator(0)]  # Stock >= 0
    )
    image_url = models.URLField(max_length=200, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        # Calculate total price
        self.total_price = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.id} for {self.product.name}"