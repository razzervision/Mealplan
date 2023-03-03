from madplan.models import Ingredients, Recipes, WeekDays
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from api.serializers import IngredientSerializer, RecipesSerializer, WeekdaysSerializer
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination


class RecipesPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_size'
    max_page_size = 1000


class IngredientsPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_size'
    max_page_size = 1000


class WeekdaysPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_size'
    max_page_size = 1000


class IngredientCreateView(ListCreateAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']
    pagination_class = IngredientsPagination


class RecipesCreateView(ListCreateAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description']
    pagination_class = RecipesPagination


class WeekdaysCreateView(ListCreateAPIView):
    queryset = WeekDays.objects.all()
    serializer_class = WeekdaysSerializer
    filter_backends = [SearchFilter]
    search_fields = ['recipes__name', 'date']
    pagination_class = WeekdaysPagination


class RecipeDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer
    lookup_field = 'pk'


class IngredientDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer
    lookup_field = 'pk'


class WeekdayDetailView(RetrieveUpdateDestroyAPIView):
    queryset = WeekDays.objects.all()
    serializer_class = WeekdaysSerializer
    lookup_field = 'pk'
