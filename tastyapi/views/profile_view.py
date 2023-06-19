from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError

from tastyapi.serializers import RecipeSerializer, RecipeTastyUserSerializer
from tastyapi.models import Recipe, Category

class ProfileView(ViewSet):
    """Profile View"""

    def list(self, request, pk=None):
        """Gets the profile information of the current user
        
        Returns:
            Response -- JSON serialized profile data
        """

        user = request.user
        user_serializer = RecipeTastyUserSerializer(user)

        profile_data = {
            'author': user_serializer.data,
            'recipe': None
        }

        recipe = Recipe.objects.filter(author=user).first()
        if recipe:
            serializer = RecipeSerializer(recipe)
            profile_data['recipe'] = serializer.data

        return Response(profile_data, status=status.HTTP_200_OK)

    def destroy_recipe(self, request):
        """Deletes the recipe of the current user"""
        user = request.user
        recipe = Recipe.objects.filter(author=user).first()

        if recipe:
            recipe.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # def update_recipe(self, request, pk):
    #     """Edit a recipe of the current user"""
    #     category = Category.objects.get(pk=request.data["category"])

    #     try:
    #         user = request.user
    #         recipe = Recipe.objects.filter(author=user, pk=pk).first()
    #         if not recipe:
    #             return Response({'message': 'Recipe not found.'}, status=status.HTTP_404_NOT_FOUND)

    #         recipe.name = request.data["name"]
    #         recipe.category = category
    #         recipe.image_path = request.data["image_path"]
    #         recipe.summary = request.data["summary"]
    #         recipe.cook_time = request.data["cook_time"]
    #         recipe.prep_time = request.data["prep_time"]
    #         recipe.total_time = request.data["total_time"]
    #         recipe.ingredients = request.data["ingredients"]
    #         recipe.preparation = request.data["preparation"]
    #         recipe.create_date = request.data["create_date"]
    #         recipe.save()

    #         serializer = RecipeSerializer(recipe)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     except ValidationError as ex:
    #         return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
