from django.contrib import admin
from .models import Ingrediens, Recipes, WeekDays

# Register your models here.
admin.site.register(Ingrediens)
admin.site.register(Recipes)
admin.site.register(WeekDays)

