from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Continent(models.Model):
    """
    Saves the continent where tour will belong
    """
    continent = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50, null=False, blank=False)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.continent


class Tour(models.Model):
    """
    Saves the tour that the customer can purchase
    """
    name = models.CharField(max_length=200, unique=True)
    meeting_location = models.CharField(max_length=50)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()
    slots = models.PositiveIntegerField(
        validators=[MinValueValidator(1)], default=1)
    slots_left = models.PositiveIntegerField(default=1)
    rating = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(10)], default=0)
    price = models.FloatField(
        validators=[MinValueValidator(0)], default=100)
    image_1 = models.ImageField(null=True, blank=True)
    image_2 = models.ImageField(null=True, blank=True)
    image_3 = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    def length(self):
        length = self.end - self.start

        return length.days

    def upon_arrival(self):
        upon_arrival = self.price * 9

        return upon_arrival

    class Meta:
        ordering = ["name"]
