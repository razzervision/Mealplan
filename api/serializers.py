from rest_framework.serializers import *
from madplan.models import Ingredients, Recipes, WeekDays


class IngredientsSerializer(ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ['id', 'name']


class RecipesSerializer(ModelSerializer):
    class Meta:
        model = Recipes
        fields = ['id', 'name', 'description', 'ingredients']


class WeekdaySerializer(ModelSerializer):
    class Meta:
        model = WeekDays
        fields = ['id', 'name', 'date']
