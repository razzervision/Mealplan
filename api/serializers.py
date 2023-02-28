from madplan.models import Ingredients, Recipes
from rest_framework import serializers


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = '__all__'

    def validate_name(self, value):
        """
        Check that the ingredient name is unique.
        """
        if Ingredients.objects.filter(name__iexact=value).exists():
            raise serializers.ValidationError('An ingredient with this name already exists.')
        return value


class RecipesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = '__all__'
