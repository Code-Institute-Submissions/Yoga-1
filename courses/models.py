from django.db import models


# Create your models here.
class Course(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    duration = models.CharField(max_length=254,
                                null=True, blank=True)
    coursedate = models.DateField(null=True, blank=True)
    coursetime = models.TimeField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    image = models.ImageField(null=True, blank=True)


def __str__(self):
    return self.name

