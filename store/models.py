from django.db import models
from core.models import BaseModel

class Category(BaseModel):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    image = models.CharField(max_length=100)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

class Brand(BaseModel):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    final_price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.CharField(max_length=200, null=True, blank=True)
    featured = models.BooleanField(default=False)
    remaining = models.SmallIntegerField(default=0)
    related_products = models.ManyToManyField('self', blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
    
    