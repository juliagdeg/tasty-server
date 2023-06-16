from rest_framework import serializers, status
from tastyapi.models import Recipe, TastyUser, Category
from django.contrib.auth.models import User

class RecipeTastyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')

# class RecipeCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ('id', 'name')

class RecipeSerializer(serializers.ModelSerializer):
    """JSON serializer for recipe posts"""

    author = RecipeTastyUserSerializer(many=False)
    # category = RecipeCategorySerializer(many=False)
    class Meta:
        model = Recipe
        fields = ('id', 'name', 'category', 'image_path', 'summary', 'cook_time', 'prep_time', 'total_time', 'ingredients', 'preparation', 'create_date', 'author')
# need to use the RecipeSerializer in my Profile View i think