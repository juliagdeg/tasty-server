from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

from tastyapi.serializers import RecipeSerializer, RecipeTastyUserSerializer
from tastyapi.models import Recipe

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

        # # Fetch the user's profile data after deleting the recipe
        # recipe = Recipe.objects.filter(author=user).first()
        # user_serializer = RecipeTastyUserSerializer(user)
        # profile_data = {
        #     'author': user_serializer.data,
        #     'recipe': RecipeSerializer(recipe).data if recipe else None
        # }
        # return Response(profile_data, status=status.HTTP_200_OK)
