from django.contrib import admin

from .models import Ingredient, \
    Recipe, \
    RecipeIngredient, \
    UnitOfMeasurement, \
    RecipeStep, \
    MealPlan, \
    MealPlanRecipe, \
    WeekDaysNative, \
    RecipesNative, \
    IngredientsNative

# Register your models here.
admin.site.register(IngredientsNative)
admin.site.register(RecipesNative)
admin.site.register(WeekDaysNative)

admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)
admin.site.register(UnitOfMeasurement)
admin.site.register(RecipeStep)
admin.site.register(MealPlan)
admin.site.register(MealPlanRecipe)
