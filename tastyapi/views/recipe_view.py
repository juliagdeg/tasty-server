from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tastyapi.models import Recipe, TastyUser, Category
from django.contrib.auth.models import User

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

    # TO-DO: Make a create method so that
    # users on the client side can create a new
        # recipe post

    def create(self, request):
        """Handles POST request for recipes"""

        # author = TastyUser.objects.get(pk=request.auth.user.id)
        # category = Category.objects.get(pk=request.data["category"])

        # recipe = Recipe.objects.create(
        #     name=request.data["name"],
        #     category=category,
        #     image_path=request.data["image_path"],
        #     summary=request.data["summary"],
            # cook_time=request.data["cook_time"],
            # prep_time=request.data["prep_time"],
            # total_time=request.data["total_time"],
            # ingredients=request.data["ingredients"],
            # preparation=request.data["preparation"],
            # create_date=request.data["create_date"],
        #     author=author
        # )

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
