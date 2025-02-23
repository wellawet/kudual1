from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Business(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    # Add more fields as needed (e.g., financial data, address)

    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # Add fields for preferences, orders, etc.

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)  # e.g., Hardware, Software
    business = models.ForeignKey(Business, on_delete=models.CASCADE)

    def __str__(self):
        return self.name