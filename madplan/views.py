from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import IngredientsForm, RecipesForm, WeekdayForm
from .models import WeekDays


def home(request):
    context = {
        'weekdays': WeekDays.objects.all(),
    }

    return render(request, 'madplan/home.html', context)


def add_weekday(request):
    if request.method == 'POST':
        form = WeekdayForm(request.POST)

        if form.is_valid():
            form.clean()
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = WeekdayForm()

    return render(request, 'madplan/add_weekday.html', {'form': form})


def add_ingredients(request):
    if request.method == 'POST':
        form = IngredientsForm(request.POST)

        if form.is_valid():
            form.clean()
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = IngredientsForm()

    return render(request, 'madplan/add_ingredients.html', {'form': form})


def add_recipes(request):
    if request.method == 'POST':
        form = RecipesForm(request.POST)

        if form.is_valid():
            form.clean()
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = RecipesForm()

    return render(request, 'madplan/add_recipes.html', {'form': form})
