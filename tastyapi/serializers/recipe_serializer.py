from rest_framework import serializers, status
from tastyapi.models import Recipe, TastyUser, Category
from django.contrib.auth.models import User

class RecipeTastyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')

class RecipeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class AddRecipeRatingSerializer(serializers.Serializer):
    score = serializers.IntegerField()

class AddRecipeCommentSerializer(serializers.Serializer):
    content = serializers.CharField()

class RecipeSerializer(serializers.ModelSerializer):
    """JSON serializer for recipe posts"""

    author = RecipeTastyUserSerializer(many=False)
    category = RecipeCategorySerializer(many=False)
    ratings = AddRecipeRatingSerializer(many=True, read_only=True)
    comments = AddRecipeCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'category', 'image_path', 'summary',
                  'cook_time', 'prep_time', 'total_time', 'ingredients', 
                  'preparation', 'create_date', 'author', 'ratings', 'comments')
