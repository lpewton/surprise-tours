from django.db import models


class message(models.Model):
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    subject = models.CharField(max_length=100, null=False, blank=False)
    message = models.CharField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.full_name
