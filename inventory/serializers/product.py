from rest_framework import serializers

from .company import CompanyShortSerializer
from .category import CategoryShortSerializer

from  ..models import Product


class ProductSerializer(serializers.ModelSerializer):

    category = CategoryShortSerializer()
    company = CompanyShortSerializer()

    class Meta:
        model = Product
        fields = ("name", "date", "photo", "cost", "store", "made_company", "inventory_number", "status", "category", "company")


class ProductCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ("name", "date", "photo", "cost", "store", "made_company", "inventory_number", "status", "category", "company")



class ProductShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ("name", "date", "photo", "inventory_number", "status")

