from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=300)
    postdate = models.DateTimeField()
