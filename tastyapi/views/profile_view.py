from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

from tastyapi.serializers import RecipeSerializer, RecipeTastyUserSerializer 
from tastyapi.models import Recipe

class ProfileView(ViewSet):
    """Profile View"""

    def list(self, request, pk=None):
        """Gets all the recipes posted by the current user
        
        NOTES - This method worked, but it did return all of the recipes
        instead of filtering, but I think that's because I don't have any conditionals
        or query.params
        """

        # user = request.user
        # recipe = Recipe.objects.filter(author=user).first()  # Retrieve the first matching recipe
        # if recipe:
        #     serializer = RecipeSerializer(recipe)
        #     return Response(serializer.data, status=status.HTTP_200_OK)
        # else:
        #     return Response(status=status.HTTP_404_NOT_FOUND)
        
        # user=request.auth.user
        # recipe = Recipe.objects.get(pk=pk, author=user)
        # if recipe:
        #     serializer = RecipeSerializer(recipe)
        #     return Response(serializer.data, status=status.HTTP_200_OK)
        # else:
        #     return Response(status=status.HTTP_404_NOT_FOUND)
        
        user = request.user
        recipe = Recipe.objects.filter(author=user).first()  # Retrieve the first matching recipe
        if recipe:
            serializer = RecipeSerializer(recipe)
            user_serializer = RecipeTastyUserSerializer(user)
            profile_data = {
                'author': user_serializer.data,
                'recipe': serializer.data
            }
            return Response(profile_data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)