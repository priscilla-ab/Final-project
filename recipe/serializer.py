from .models import Recipe ,Category , Ingredient
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class Categoryserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name","slug","type")
    
class Ingredientserializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"
        
class Recipeserializer(serializers.ModelSerializer):
    category = serializers.CharField(source = "category.name")
    ingredient = Ingredientserializer(read_only=True, many=True)
    class Meta:
        model = Recipe
        fields = "__all__"