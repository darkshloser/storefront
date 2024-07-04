from decimal import Decimal
from store.models import Product, Collection
from rest_framework import serializers


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
        
