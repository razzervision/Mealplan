from django.urls import path
from api.views import IngredientCreateView, RecipesView, RecipeDetailView

urlpatterns = [
    path('ingredients/', IngredientCreateView.as_view(), name='ingredient_create'),
    path('recipes/', RecipesView.as_view(), name='recipes_get'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
]
