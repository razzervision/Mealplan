from django.db import models
from django.contrib.auth.models import User
from rest_framework.reverse import reverse


# Create your models here.
class IngredientsNative(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class RecipesNative(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    ingredients = models.ManyToManyField(IngredientsNative)

    def __str__(self):
        return self.name


class WeekDaysNative(models.Model):
    recipes = models.ForeignKey(RecipesNative, on_delete=models.CASCADE)
    date = models.DateField('%d-%m-%y')

    def __str__(self):
        return f'{str(self.date)}'


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    brand = models.CharField(max_length=100, blank=True)
    calories_per_100g = models.DecimalField(max_digits=6, decimal_places=2)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ingredient_detail', args=[str(self.slug)])


class Recipe(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')
    is_private = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=6, decimal_places=2)
    unit = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.ingredient.name} ({self.quantity} {self.unit})'


class UnitOfMeasurement(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=10)
    conversion_factor = models.DecimalField(max_digits=8, decimal_places=4)

    def __str__(self):
        return self.name


class RecipeStep(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    step_number = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f'{self.recipe.name} - Step {self.step_number}'


class MealPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    recipes = models.ManyToManyField(Recipe, through='MealPlanRecipe')

    def __str__(self):
        return f'{self.user.username} - {self.name}'


class MealPlanRecipe(models.Model):
    meal_plan = models.ForeignKey(MealPlan, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    day = models.DateField()

    def __str__(self):
        return f'{self.meal_plan.name} - {self.recipe.name} - {self.day}'
