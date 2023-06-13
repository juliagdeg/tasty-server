from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tastyapi.models import Recipe, TastyUser, Category

class RecipeView(ViewSet):
    """Recipe Post View"""

    def list(self, request):
        """Handles GET requests to retrieve all recipe posts
        
        Returns:
            Response -- JSON serialized list of recipes
        """

        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk):
        """Handles GET request for a single recipe post
        
        Returns -- JSON serialized post
        """

        recipe = Recipe.objects.get(pk=pk)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

class RecipeTastyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TastyUser
        fields = ('id', 'full_name')

class RecipeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class RecipeSerializer(serializers.ModelSerializer):
    """JSON serializer for recipe posts"""

    author = RecipeTastyUserSerializer(many=False)
    category = RecipeCategorySerializer(many=False)
    class Meta:
        model = Recipe
        fields = ('id', 'name', 'category', 'image_path', 'summary', 'cook_time', 'prep_time', 'total_time', 'ingredients', 'preparation', 'create_date', 'author')
