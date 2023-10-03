from django.shortcuts import render
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer, CouponSerializer, ProductOrderSerializer, AddressSerializer, OrderSerializer, CommentSerializer, FavoritSerializer
from .models import Category, Brand, Product, Coupon, ProductOrder, Address, Order, Comment, Favorit
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BrandView(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CouponView(ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

class ProductOrderView(ModelViewSet):
    queryset = ProductOrder.objects.all()
    serializer_class = ProductOrderSerializer

class AddressView(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class OrderView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class FavoritView(ModelViewSet):
    queryset = Favorit.objects.all()
    serializer_class = FavoritSerializer