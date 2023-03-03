from madplan.models import Ingredients, Recipes, WeekDays
from rest_framework import serializers


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = '__all__'

    def create(self, validated_data):
        name = validated_data.get('name')
        if Ingredients.objects.filter(name=name).exists():
            raise serializers.ValidationError('Ingredient already exists')
        return super().create(validated_data)


class RecipesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = '__all__'


class WeekdaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeekDays
        fields = '__all__'
