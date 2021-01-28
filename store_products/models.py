from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=200)
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Brand(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    logo = models.ImageField(default="brand.jpg", upload_to="brands")
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    usual_price = models.FloatField()
    listing_price = models.FloatField()
    description = models.TextField()
    picture = models.ImageField(upload_to="products", default="products/default.jpg")

    def __str__(self):
        return self.name

class Size(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=10)

    def __str__(self):
        return self.size

class Color(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.color

class Spec(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    value = models.CharField(max_length=200)

    def __str__(self):
        return self.value

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    rating = models.IntegerField()
    comment = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.comment

class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products")

    def __str__(self):
        return self.image.name

