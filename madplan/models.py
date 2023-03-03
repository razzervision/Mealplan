from django.db import models


# Create your models here.
class Ingredients(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Recipes(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredients)

    def __str__(self):
        return self.name


class WeekDays(models.Model):
    recipes = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    date = models.DateField('%d-%m-%y')

    def __str__(self):
        return f'{str(self.date)}'

