from django import forms

from . import models


class IngredientsForm(forms.ModelForm):
    class Meta:
        model = models.IngredientsNative
        fields = ['name']


class RecipesForm(forms.ModelForm):
    class Meta:
        model = models.RecipesNative
        fields = ['name', 'description', 'ingredients']


class WeekdayForm(forms.ModelForm):
    class Meta:
        model = models.WeekDaysNative
        fields = ['recipes', 'date']
