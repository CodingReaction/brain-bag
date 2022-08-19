from django.db import models
from django.utils import timezone


class Bag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Term(models.Model):
    bag = models.ForeignKey(Bag, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=200, blank=True)
    is_finished = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name