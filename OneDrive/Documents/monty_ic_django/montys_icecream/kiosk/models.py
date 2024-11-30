from django.db import models

class Flavor(models.Model):
    flavor = models.CharField(max_length=100)

    def __str__(self):
        return self.flavor


class IceCreamType(models.Model):
    type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.type


class Topping(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name