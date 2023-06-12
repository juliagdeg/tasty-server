from django.db import models
from django.contrib.auth.models import User

class Favorite(models.Model):
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# might have to add f string to show what is favorited by whom
