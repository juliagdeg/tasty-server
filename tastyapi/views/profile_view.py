from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from tastyapi.serializers import TastyUserSerializer, RecipeSerializer
from tastyapi.models import Recipe, TastyUser

# list method get user's profile
class ProfileView(ViewSet):
    
    @action(methods=['GET'], detail=False)
    def profile(self, request):
        try:
            serializer = TastyUserSerializer(request.user)
            return Response(serializer.data)
        except TastyUser.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    @action(methods=['GET'], detail=False)
    def my_recipes(self, request):
        user = request.user
        recipes = Recipe.objects.filter(author__user=user)
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
# before EOD, a postman get did not return profile. trying to determine how to remedy this