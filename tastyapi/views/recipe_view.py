from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tastyapi.models import Recipe, TastyUser, Category
from django.contrib.auth.models import User

from tastyapi.serializers import RecipeSerializer

class RecipeView(ViewSet):
    """Recipe Post View"""

    def destroy(self, request, pk):
        """Deletes a recipe"""
        recipe = Recipe.objects.get(pk=pk)
        recipe.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

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

    # TO-DO: Make a create method so that
    # users on the client side can create a new
        # recipe post

    def create(self, request):
        """Handles POST request for recipes"""

        new_recipe = Recipe()
        new_recipe.name = request.data["name"]
        new_recipe.category = Category.objects.get(pk=request.data["category"])
        new_recipe.image_path = request.data["image_path"]
        new_recipe.summary = request.data["summary"]
        new_recipe.cook_time=request.data["cook_time"]
        new_recipe.prep_time=request.data["prep_time"]
        new_recipe.total_time=request.data["total_time"]
        new_recipe.ingredients=request.data["ingredients"]
        new_recipe.preparation=request.data["preparation"]
        new_recipe.create_date=request.data["create_date"]
        new_recipe.author=User.objects.get(pk=request.auth.user.id)
        new_recipe.save()

        serializer = RecipeSerializer(new_recipe)
        return Response(serializer.data)

    # TO-DO: Recipes will need to be filtered by category - query.param
