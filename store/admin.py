from django.contrib import admin
from .models import Promotion, Collection, Cart, Customer, Product, Order, OrderItem, Address, CartItem


admin.site.register(Promotion)
admin.site.register(Collection)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Address)
admin.site.register(CartItem)