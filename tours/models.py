from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Continent(models.Model):
    continent = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.continent

class Tour(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=50)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    slots = models.PositiveIntegerField(
        validators=[MinValueValidator(1)], default=1)
    slots_left = models.PositiveIntegerField(default=1)
    description = models.CharField(max_length=254)
    rating = models.FloatField(
        validators=[MinValueValidator(0)], default=0)
    image_1 = models.ImageField(null=True, blank=True)
    image_2 = models.ImageField(null=True, blank=True)
    image_3 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name