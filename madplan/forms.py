from django import forms

from . import models


class IngredientsForm(forms.ModelForm):
    class Meta:
        model = models.Ingredients
        fields = ['name']


class RecipesForm(forms.ModelForm):
    class Meta:
        model = models.Recipes
        fields = ['name', 'description', 'ingredients']


class WeekdayForm(forms.ModelForm):
    class Meta:
        model = models.WeekDays
        fields = ['recipes', 'date']
