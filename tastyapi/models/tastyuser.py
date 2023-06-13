from django.db import models
from django.contrib.auth.models import User

class TastyUser(models.Model):
    bio = models.CharField(max_length=300)
    profile_image_url = models.URLField()
    created_on = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

# add a property for full name later after running client side
    @property
    def full_name(self):
        """converts first/last name field into 
        a single property string"""
        return f'{self.user.first_name} {self.user.last_name}'
