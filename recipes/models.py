from django.db import models
from category.models import Category

# Create your models here.

class Recipes(models.Model):
    recipe_name = models.CharField(max_length=1000)
    prep_time = models.CharField(max_length=200, blank=True , null=True)
    cook_time = models.CharField(max_length=200, blank=True, null=True)
    total_time = models.CharField(max_length=200, blank=True, null=True)
    servings = models.CharField(max_length=300, blank=True, null=True)
    yields = models.CharField(max_length=100, blank=True, null=True)
    ingredients = models.CharField(max_length=1000, blank=True)
    directions = models.TextField(max_length=10000, blank=True)
    rating = models.FloatField(max_length=5, blank=True)
    url = models.URLField(max_length=1000, blank=True)
    cuisine_path = models.CharField(max_length=100, blank=True)
    nutrition = models.CharField(max_length=1000, blank=True)
    timing = models.CharField(max_length=1000, blank=True, null=True)
    img_src = models.URLField(max_length=1000, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    #created_date = models.DateTimeField(auto_now_add=True)
    #modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'recipe'
        verbose_name_plural = 'recipes'

    def __str__(self):
        return self.recipe_name

