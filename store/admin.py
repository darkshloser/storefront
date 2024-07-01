from django.contrib import admin, messages
from django.contrib.contenttypes.admin import GenericTabularInline
from django.db.models.aggregates import Count
from django.db.models.query import QuerySet
from django.utils.html import format_html, urlencode
from django.urls import reverse
from .models import Promotion, Collection, Cart, Customer, Product, Order, OrderItem, Address, CartItem


admin.site.register(Collection)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price']
    list_editable = ['unit_price']
    list_per_page = 10

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 10


admin.site.register(Promotion)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Address)
admin.site.register(CartItem)