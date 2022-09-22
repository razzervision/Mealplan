from django.http import JsonResponse
from madplan.models import Ingredients, Recipes, WeekDays
from api.serializers import IngredientsSerializer, RecipesSerializer, WeekdaySerializer


def ingredients_list(request):
    ingredients = Ingredients.objects.all()
    serializer = IngredientsSerializer(ingredients, many=True)
    return JsonResponse(serializer.data, safe=False)


def recipes_list(request):
    recipe = Recipes.objects.all()
    serializer = RecipesSerializer(recipe, many=True)
    return JsonResponse(serializer.data, safe=False)


def weekday_list(request):
    weekday = WeekDays.objects.all()
    serializer = WeekdaySerializer(weekday, many=True)
    return JsonResponse(serializer.data, safe=False)
