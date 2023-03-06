from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from madplan.models import Ingredient, Recipe, RecipeIngredient, UnitOfMeasurement, RecipeStep, MealPlan, MealPlanRecipe
from .serializers import IngredientSerializer, RecipeSerializer, RecipeIngredientSerializer, \
    UnitOfMeasurementSerializer, RecipeStepSerializer, MealPlanSerializer, MealPlanRecipeSerializer, UserSerializer
from rest_framework import pagination


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all().order_by('name')
    serializer_class = IngredientSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all().order_by('name')
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination


class RecipeIngredientViewSet(viewsets.ModelViewSet):
    queryset = RecipeIngredient.objects.all().order_by('recipe')
    serializer_class = RecipeIngredientSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination


class UnitOfMeasurementViewSet(viewsets.ModelViewSet):
    queryset = UnitOfMeasurement.objects.all().order_by('name')
    serializer_class = UnitOfMeasurementSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination


class RecipeStepViewSet(viewsets.ModelViewSet):
    queryset = RecipeStep.objects.all().order_by('recipe')
    serializer_class = RecipeStepSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination


class MealPlanViewSet(viewsets.ModelViewSet):
    queryset = MealPlan.objects.all().order_by('name')
    serializer_class = MealPlanSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination


class MealPlanRecipeViewSet(viewsets.ModelViewSet):
    queryset = MealPlanRecipe.objects.all().order_by('recipe')
    serializer_class = MealPlanRecipeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination
