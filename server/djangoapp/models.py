# Uncomment the following imports before adding the Model code

from django.db import models
#from django.utils.timezone import now
#from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=50)
    
    description = models.CharField(null=True, max_length=500)

    def __str__(self):
        return self.name

# Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
    make = models.ForeignKey(CarMake, null=True, on_delete = models.CASCADE)

    dealer_id = models.IntegerField()
    name = models.CharField(max_length=255)
    SEDAN = "Sedan"
    SUV = "SUV"
    WAGON = "WAGON"
    TYPE_CHOICES = (
        (SEDAN, "Sedan"),
        (SUV, "SUV"),
        (WAGON, "Wagon"),
    )
    model_type  = models.CharField(max_length=10, choices=TYPE_CHOICES)
    year = models.DateField()

    def __str__(self):
        return f"{self.make} {self.name} ({self.year})"
