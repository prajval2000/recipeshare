from django.shortcuts import render
from .models import Recipes

# Create your views here.

def recipe(request,id):
    recipe = Recipes.objects.get(id=id)

    similar_recipes =[]

    x = range(int(id)+1, int(id)+5)
    for n in x: 
        similar_recipes.append(Recipes.objects.get(id=str(n)))

    ingredients_list = recipe.ingredients.split(',')
    nutritions_list = recipe.nutrition.split(',')
    context = {
        'recipe': recipe,
        'ingredients': ingredients_list,
        'nutritions': nutritions_list,
        'similar': similar_recipes,
    }
    return render(request, 'recipe/recipe_detail.html', context)