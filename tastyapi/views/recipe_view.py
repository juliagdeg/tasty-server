from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tastyapi.models import Recipe, TastyUser, Category
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import action

from tastyapi.models import Rating, Comment

from tastyapi.serializers import RecipeSerializer

class RecipeView(ViewSet):
    """Recipe Post View"""

    def update(self, request, pk):
        """Edit a recipe of the current user"""
        category = Category.objects.get(pk=request.data['category'])

        recipe = Recipe.objects.get(
            pk=pk, author=request.auth.user)
        recipe.name = request.data['name']
        recipe.name = request.data["name"]
        recipe.category = category
        recipe.image_path = request.data["image_path"]
        recipe.summary = request.data["summary"]
        recipe.cook_time=request.data["cook_time"]
        recipe.prep_time=request.data["prep_time"]
        recipe.total_time=request.data["total_time"]
        recipe.ingredients=request.data["ingredients"]
        recipe.preparation=request.data["preparation"]
        recipe.create_date=request.data["create_date"]
        recipe.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        # except Recipe.DoesNotExist as ex:
        #     return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        """Deletes a recipe"""
        try:
            recipe = Recipe.objects.get(
                pk=pk, author=request.auth.user)
            recipe.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Recipe.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

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

    @action(methods=['post'], detail=True, url_path='rate-recipe')
    def rate_recipe(self, request, pk):
        """Rate a recipe"""
        recipe = Recipe.objects.get(pk=pk)

        try:
            rating = Rating.objects.get(
                user=request.auth.user, recipe=recipe
            )
            rating.score = request.data['score']
            rating.save()
            return Response({'message': 'Rating updated'}, status=status.HTTP_200_OK)
        except Rating.DoesNotExist:
            Rating.objects.create(
                user=request.auth.user,
                recipe=recipe,
                score=request.data['score']
            )
            return Response({'message': 'Rating added'}, status=status.HTTP_201_CREATED)

    @action(methods=['post'], detail=True, url_path='recipe-comments')
    def add_recipe_comment(self, request, pk):
        """Comment on a recipe"""
        recipe = Recipe.objects.get(pk=pk)

        try:
            comment = Comment.objects.get(
                user=request.auth.user, recipe=recipe
            )
            comment.content = request.data['content']
            comment.postdate=request.data['postdate']
            comment.save()
        except Comment.DoesNotExist:
            comment = Comment.objects.create(
                user=request.auth.user,
                recipe=recipe,
                content=request.data['content'],
                postdate=request.data['postdate']
            )

        return Response({'message': 'Comment added'}, status=status.HTTP_201_CREATED)
    
    # @action(methods=['post'], detail=True, url_path='rate-recipe')
    # def rate_recipe(self, request, pk):
    #     """Rate a recipe"""
    #     recipe = Recipe.objects.get(pk=pk)

    #     try:
    #         rating = Rating.objects.get(
    #             user=request.auth.user, recipe=recipe
    #         )
    #         rating.score = request.data['score']
    #         rating.save()
    #     except Rating.DoesNotExist:
    #         rating = Rating.objects.create(
    #             user=request.auth.user,
    #             recipe=recipe,
    #             score=request.data['score']
    #         )

    #     return Response({'message': 'Rating added'}, status=status.HTTP_201_CREATED)
    # TO-DO: Recipes will need to be filtered by category - query.param
