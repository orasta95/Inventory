from rest_framework import serializers

from  ..models import Category


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ("name", "parent")


class CategoryCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ("name", "parent")



class CategoryShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ("name", "parent")

