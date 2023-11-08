from django.contrib import admin
from .models import Recipes

# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('recipe_name','category', 'rating',)

admin.site.register(Recipes, RecipeAdmin)