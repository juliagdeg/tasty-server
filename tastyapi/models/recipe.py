from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    image_path = models.CharField(max_length=300)
    summary = models.CharField(max_length=300)
    cook_time = models.CharField(max_length=50)
    prep_time = models.CharField(max_length=50)
    total_time = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=300)
    preparation = models.TextField(max_length=3000, null=True)
    create_date = models.DateField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.ManyToManyField("Comment", through="RecipeComment", related_name='comments')
