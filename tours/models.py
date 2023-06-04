from django.db import models

class Continent(models.Model):
    continent = models.CharField(max_length=254)

    def __str__(self):
        return self.continent
