from django.urls import path
from api.views import IngredientCreateView, \
    RecipesCreateView, \
    RecipeDetailView, \
    WeekdaysCreateView, \
    WeekdayDetailView, \
    IngredientDetailView

urlpatterns = [
    path('ingredients/', IngredientCreateView.as_view(), name='ingredient_CreateView'),
    path('ingredients/<int:pk>/', IngredientDetailView.as_view(), name='ingredient_detail'),
    path('recipes/', RecipesCreateView.as_view(), name='recipes_CreateView'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('weekdays/', WeekdaysCreateView.as_view(), name='weekdays_CreateView'),
    path('weekdays/<int:pk>/', WeekdayDetailView.as_view(), name='weekday_detail'),

]
