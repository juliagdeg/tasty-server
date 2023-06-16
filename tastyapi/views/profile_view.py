from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

from tastyapi.serializers import RecipeSerializer
from tastyapi.models import Recipe, TastyUser

class ProfileView(ViewSet):
    """Profile View"""

    def list(self, request):
        """Gets all the recipes posted by the current user
        
        NOTES - This method worked, but it did return all of the recipes
        instead of filtering, but I think that's because I don't have any conditionals
        or query.params
        """

        user = request.user
        recipes = Recipe.objects.filter(author=user)
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # def my_profile(self, request, pk=None):
    #     recipe = Recipe.objects.get(pk=pk)

    #     try:
    #         profile = TastyUser.objects.get(
    #             user=request.auth.user
    #         )

    # @action(methods=['GET'], detail=False)
    # def profile(self, request):
    #     try:
    #         serializer = TastyUserSerializer(request.user)
    #         return Response(serializer.data)
    #     except TastyUser.DoesNotExist as ex:
    #         return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    # @action(methods=['GET'], detail=False)
    # def my_recipes(self, request):
        # user = request.user
        # recipes = Recipe.objects.filter(author__user=user)
        # serializer = RecipeSerializer(recipes, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)
# before EOD, a postman get did not return profile. trying to determine how to remedy this
