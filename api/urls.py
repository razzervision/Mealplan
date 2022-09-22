from django.urls import path
from api.views import ingredients_list, recipes_list, weekday_list

urlpatterns = [
    path('ingredients', ingredients_list),
    path('recipes', recipes_list),
    path('weekday', weekday_list)
]
