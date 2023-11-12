from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("recipe_details/<id>/", views.recipe_detail, name="recipe_detail"),
    path('', views.all_recipes, name='all_recipes'),
    path('<slug:category_slug>/', views.all_recipes, name='recipes_by_category'),
    path('upload_recipe', views.upload_recipe, name='upload_recipe')

]