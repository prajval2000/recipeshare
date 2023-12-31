from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("recipe_details/<id>/", views.recipe_detail, name="recipe_detail"),
    path('', views.all_recipes, name='all_recipes'),
    path('category/<slug:category_slug>/', views.all_recipes, name='recipes_by_category'),
    path('search/', views.search, name='search'),

    path('upload_recipe', views.upload_recipe, name='upload_recipe'),
    path('user_recipes', views.user_recipes, name='user_recipes'),
    path("user_recipe_details/<id>/", views.user_recipe_detail, name="user_recipe_detail"),

]