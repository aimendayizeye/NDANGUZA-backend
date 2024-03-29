from django.db.models import fields
from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "price",
            "description",
            "get_absolute_url",
            "get_image",
            "get_thumbnail"
        )

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Category
        fields = (
            "id","name","get_absolute_url","products",
        )