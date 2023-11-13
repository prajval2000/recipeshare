from django.contrib import admin
from .models import Recipes, UserRecipe

# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('recipe_name','category', 'rating',)

class UserRecipeAdmin(admin.ModelAdmin):
    list_display = ('recipe_name','category',)

admin.site.register(Recipes, RecipeAdmin)
admin.site.register(UserRecipe, UserRecipeAdmin)