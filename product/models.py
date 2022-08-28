from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    discountPercentage = models.FloatField()
    rating = models.FloatField()
    stock = models.IntegerField()
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    thumbnail = models.CharField(max_length=100)
    images = models.JSONField()
    
    def __str__(self):
        return self.title