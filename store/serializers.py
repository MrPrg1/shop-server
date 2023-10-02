from rest_framework.serializers import ModelSerializer
from .models import Category, Brand, Product, Coupon, ProductOrder, Address, Order, Comment, Favorit


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CouponSerializer(ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'

class ProductOrderSerializer(ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = '__all__'

class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class FavoritSerializer(ModelSerializer):
    class Meta:
        model = Favorit
        fields = '__all__'