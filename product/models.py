from django.db import models

# Create your models here.
class Product(models.Model):
    name    = models.CharField(max_length=50)
    price   = models.FloatField()
    amount  = models.IntegerField(null=True,blank=True)