from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    image_path = models.URLField()
    summary = models.CharField(max_length=300)
    cook_time = models.CharField(max_length=50)
    prep_time = models.CharField(max_length=50)
    total_time = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=300)
    preparation = models.TextField(max_length=3000, null=True)
    create_date = models.DateField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # TO-DO: Add a user_rating custom property

    # TO-DO: Add an avg_rating custom property
    @property
    def average_rating(self):
        """Average rating calculated attribute for each recipe
        Returns:
            number --- the avg rating for a recipe
        """

        total_rating = 0
        ratings_count = self.ratings.count()

        if ratings_count != 0:
            for rating in self.ratings.all():
                total_rating += rating.score

            avg = total_rating / self.ratings.count()

        else:
            avg = 0

        return avg
