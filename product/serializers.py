from rest_framework import serializers
from .models import Category, Product, Review

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'text', 'product', 'stars', ]

class ProductReviewSerializers(serializers.ModelSerializer):
    product_review = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = 'title product_review'.split()


class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1)
    description = serializers.CharField(min_length=1, required=False)
    price = serializers.FloatField(min_value=0)
    category_id = serializers.IntegerField(min_value=1)

class CategoryValidateSerializers(serializers.Serializer):
    name = serializers.CharField(min_length=1)


class ReviewValidateSerializers(serializers.Serializer):
    text = serializers.CharField(min_length=1)
    product_id = serializers.IntegerField(min_value=1)
    stars = serializers.IntegerField(min_value=1)

