from django.db import models

class Cars(models.Model):
    number = models.CharField(max_length = 6)
    model = models.CharField(max_length = 50)
    price = models.IntegerField()