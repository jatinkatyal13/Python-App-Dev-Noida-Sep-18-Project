from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(unique = True)

    def __str__ (self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey('Category', on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)
    price = models.FloatField()

    def __str__ (self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey('Product', on_delete = models.CASCADE)
    content = models.TextField()
    author = models.CharField(max_length = 100)

    def __str__ (self):
        return self.author