from rest_framework import serializers
from tastyapi.models import TastyUser
from django.contrib.auth.models import User
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from tastyapi.serializers import TastyUserSerializer

class TastyUsersView(ViewSet):
    """TastyUser view"""
    def list(self, request):
        """Handles GET request to get all users"""
        tasty_users = TastyUser.objects.all()

        serializer = TastyUserSerializer(tasty_users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET request for single user detail"""
        try:
            tasty_user = TastyUser.objects.get(pk=pk)
            serializer = TastyUserSerializer(tasty_user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except TastyUser.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
