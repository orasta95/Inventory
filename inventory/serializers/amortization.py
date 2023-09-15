from rest_framework import serializers


from .product import ProductShortSerializer
from ..models import Amortization


class AmortizationSerializer(serializers.ModelSerializer):
    product = ProductShortSerializer()
    
    class Meta:
        model = Amortization
        fields = ("product", "expire_year")


class AmortizationCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Amortization
        fields = ("product", "expire_year")



class AmortizationShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Amortization
        fields = ("product", "expire_year")

