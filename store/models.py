from typing import Any
from django.core.validators import MinValueValidator
from django.db import models


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    # field 'product_set' will be created where it will return all the products particular promotion is aplied to 


class Collection(models.Model):
    title = models.CharField(max_length=255)
    feature_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+', blank=True)  # if we specify related_name='+' this tells Django not to create reverce relationship

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['first_name', 'last_name']


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    unit_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(1, message="Greater or equal to 1")])                    # Always to be used for monetary values 9999.99
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)                           # Django will automatically stores the current datetime here
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT, related_name='products')        # if you delete collection to NOT delete all the products in thet collection
    promotions = models.ManyToManyField(
        Promotion,
        related_name='product_set',
        blank=True
    )  # Django is going to create reverse relationship in the Promotion class

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['title']


class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    ]

    placed_at = models.DateTimeField(auto_now_add=True)         # first time we create an Order django automatically populates this field 
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)    # if we accidently delete a customer to not delete the orders


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)        # if we delete an Order to not delete OrderItem
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='orderitems')
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)    # price of products can change over time so we should always store the price


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)     # when we delete a customer associated address will also be deleted (if SET_NULL then address will not be deleted from database)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)    # if we delete a product, that product should be deleted from all the existing shopping carts as well
    quantity = models.PositiveSmallIntegerField()


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')  # if you delete a product all its reviews will be deleted automatically
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)  # it will be automatically populated 

