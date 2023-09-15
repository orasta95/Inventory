from rest_framework import serializers

from  ..models import Company


class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Company
        fields = ("name")


class CompanyCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ("name")



class CompanyShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ("name")

