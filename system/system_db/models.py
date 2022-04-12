from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)


class Product(models.Model):
    name = models.CharField(max_length=128)


class Status(models.Model):
    name = models.CharField(max_length=30)
    style_class = models.TextField()


class ActualOrder(models.Model):
    number = models.IntegerField()
    product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)


