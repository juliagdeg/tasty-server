from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from tastyapi.views import register_user, login_user, RecipeView, CategoryView, TastyUsersView, ProfileView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"recipes", RecipeView, "recipe")
router.register(r"categories", CategoryView, "category")
router.register(r'profile', ProfileView, 'profile')
router.register(r'tasty-users', TastyUsersView, 'user')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
]
