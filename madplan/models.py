from django.db import models


# Create your models here.
class Ingrediens(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Recipes (models.Model):
    name = models.CharField(max_length=30)
    descripton = models.CharField(max_length=500)
    ingrediens = models.ManyToManyField(Ingrediens)

    def __str__(self):
        return self.name


class WeekDays (models.Model):
    recipes = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    date = models.DateTimeField('%d-%m-%y')

    def __str__(self):
        return f'{str(self.date)}'
