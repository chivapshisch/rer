from django.db import models


class Types(models.Model):
    typer = models.CharField(max_length = 200)

    def __str__(self):
        return self.typer
    class Meta:
        verbose_name = 'Модель автомобиля'
        verbose_name_plural = 'Модель автомобиля'

class Status(models.Model):
    polozhenie = models.CharField(max_length = 8)
    def __str__(self):
        return self.polozhenie
    
    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статус'

class Gorod(models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city
    
    class Meta:
        verbose_name = 'Города'
        verbose_name_plural = 'Города'

class Cars(models.Model):
    town = models.ForeignKey(Gorod, on_delete= models.CASCADE)
    number = models.CharField(max_length = 6)
    model = models.ForeignKey(Types, on_delete= models.CASCADE)
    price = models.IntegerField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    cvet = models.CharField(max_length=150)
    god_vypuska = models.IntegerField()

    def __str__(self):
        return self.number
    
    class Meta:
        verbose_name = 'Машины'
        verbose_name_plural = 'Машины'

