from decimal import Decimal
from rest_framework import serializers
from .models import Product, Collection, Review, Cart, CartItem


# class CollectionSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'inventory', 'unit_price', 'price_with_tax','collection']  # by default Model serializer use primary key related fields
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # price = serializers.DecimalField(max_digits=6, decimal_places=2, source='unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    # # collection = CollectionSerializer()
    # collection = serializers.HyperlinkedRelatedField(
    #     queryset=Collection.objects.all(),
    #     view_name='collection-detail'
    # )   #  "collection": "http://127.0.0.1:8000/store/coections/3/"

    def calculate_tax(self, product: Product) -> Decimal:
        return product.unit_price * Decimal(1.1)
    
    # Override how object is created
    def create(self, validated_data):
        product = Product(**validated_data)
        product.save()
        return product
    
    #Override when updating an object
    def update(self, instance: Product, validated_data):
        # instance - product object
        # validated_data - data of the object
        instance.unit_price = validated_data.get('unit_price')
        instance.save()
        return instance
    
    # We can override 'validate' method in order to have a custom validation NOT only the one from our model
    # def validate(self, data):
    #     if data['password'] != data['confirm_password']:
    #         return serializers.ValidationError('Passwords do not match!')
    #     return data



class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    products_count = serializers.IntegerField(read_only=True)  # We can define read-only fields which are not used for creation or update


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'date', 'name', 'description', 'product']


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)              # If we don't want to define it when we create a new record we create this line with 'read_only=True'
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'created_at']




