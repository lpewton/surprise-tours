from django.db import models

class Continent(models.Model):
    continent = models.CharField(max_length=254)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.continent
