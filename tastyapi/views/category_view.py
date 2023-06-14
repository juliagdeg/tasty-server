from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tastyapi.models import Category

class CategoryView(ViewSet):
    """Recipe Post View"""

    def list(self, request):
        """Handles GET requests to retrieve all recipe posts
        
        Returns:
            Response -- JSON serialized list of recipes
        """

        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk):
        """Handles GET request for a single recipe post
        
        Returns -- JSON serialized post
        """

        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
