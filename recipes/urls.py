from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("recipe_details/<id>/", views.recipe, name="recipe_detail"),
]