from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=1000, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name