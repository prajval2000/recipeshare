from django.shortcuts import render, get_object_or_404
from .models import Recipes
from category.models import Category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def all_recipes(request, category_slug=None):
    categories = None
    recipes = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        recipes = Recipes.objects.filter(category=categories)
    else:
        recipes = Recipes.objects.all()
    
    paginator = Paginator(recipes,15)
    page = request.GET.get('page')
    paged_recipes = paginator.get_page(page)
    context={
        'recipes' : paged_recipes
    }
    return render(request, 'recipe/all_recipes.html', context)


def recipe_detail(request,id):
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

def upload_recipe(request):
    return render(request, 'recipe/upload_recipe.html')