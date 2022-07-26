from django.shortcuts import render
from .models import WeekDays, Recipes, Ingrediens


def home(request):

    context = {
        'weekdayes': WeekDays.objects.all(),
        'recipes': Recipes.objects.all(),
        'ingrediens': Ingrediens.objects.all()
    }

    return render(request, 'madplan/home.html', context)
