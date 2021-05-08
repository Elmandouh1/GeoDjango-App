from django.db import models

# Create your models here.
class Measurement(models.Model):
    location = models.CharField(max_length=500)
    destination = models.CharField(max_length=500)
    distance = models.DecimalField(max_digits=9, decimal_places=2)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return f'The Distance between {self.location} and {self.destination} is {self.distance} KM'
    