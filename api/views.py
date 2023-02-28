from madplan.models import Ingredients, Recipes
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from api.serializers import IngredientSerializer, RecipesSerializer
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination


class RecipesPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_size'
    max_page_size = 1000


class IngredientCreateView(ListCreateAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer


class RecipesView(ListCreateAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description']
    pagination_class = RecipesPagination


class RecipeDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer
    lookup_field = 'pk'
