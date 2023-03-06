from madplan.models import Ingredient, Recipe, RecipeIngredient, UnitOfMeasurement, RecipeStep, MealPlan, MealPlanRecipe
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'brand', 'calories_per_100g', 'slug']
        read_only_fields = ['id']

    def create(self, validated_data):
        name = validated_data.get('name')
        if Ingredient.objects.filter(name=name).exists():
            raise serializers.ValidationError('Ingredient already exists')
        return super().create(validated_data)


class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer()

    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity', 'unit']


class RecipeStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeStep
        fields = ['step_number', 'description']


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = RecipeIngredientSerializer(many=True, read_only=True)
    steps = RecipeStepSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'description', 'ingredients', 'steps', 'is_private', 'user', 'slug', 'url']
        read_only_fields = ['id']

    def create(self, validated_data):
        name = validated_data.get('name')
        if Recipe.objects.filter(name=name).exists():
            raise serializers.ValidationError('Recipe already exists')
        return super().create(validated_data)


class UnitOfMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitOfMeasurement
        fields = '__all__'


class MealPlanRecipeSerializer(serializers.ModelSerializer):
    recipe = RecipeSerializer()

    class Meta:
        model = MealPlanRecipe
        fields = ['id', 'recipe', 'day']


class MealPlanSerializer(serializers.ModelSerializer):
    recipes = MealPlanRecipeSerializer(many=True, read_only=True)

    class Meta:
        model = MealPlan
        fields = ['id', 'user', 'name', 'start_date', 'end_date', 'recipes']
        read_only_fields = ['id', 'user']
