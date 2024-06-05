from django.db import models

# Create your models here.

class Owner(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Car(models.Model):
    owner = models.OneToOneField(Owner, on_delete=models.CASCADE)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"