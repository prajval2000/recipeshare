from django.shortcuts import render, get_object_or_404,redirect
from .models import Recipes, UserRecipe
from accounts.models import UserProfile
from category.models import Category
from django.contrib.auth.models import User
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

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
    userprofile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        recipe_name         = request.POST['recipe_name']
        prep_time           = request.POST['prep_time']
        cook_time           = request.POST['cook_time']
        total_time          = request.POST['total_time']
        servings            = request.POST['servings']
        yields              = request.POST['yields']
        ingredients         = request.POST['ingredients']
        directions          = request.POST['directions']
        cuisine_path        = request.POST['cuisine_path']
        nutrition           = request.POST['nutrition']
        img_src             = request.FILES['img_src']
        category_id         = request.POST['category_id']

        

        new_recipe = UserRecipe.objects.create(
            user_id = userprofile.user_id,
            recipe_name = recipe_name,
            prep_time = prep_time,
            cook_time = cook_time,
            total_time= total_time,
            servings= servings,
            yields = yields,
            ingredients = ingredients,
            directions = directions,
            cuisine_path = cuisine_path,
            nutrition= nutrition,
            img_src = img_src,
            category_id = category_id,
        )
        new_recipe.save()

        return redirect('profile')
    else:
        return render(request, 'recipe/upload_recipe.html')
    

def user_recipes(request, category_slug=None):
    categories = None
    recipes = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        recipes = UserRecipe.objects.filter(category=categories)
    else:
        recipes = UserRecipe.objects.all()
    
    context={
        'recipes' : recipes
    }

    return render(request, 'recipe/user_recipes.html', context)

def user_recipe_detail(request,id):
    userprofile = get_object_or_404(UserProfile, user=request.user)
    recipe = UserRecipe.objects.get(id=id)

    other_recips = UserRecipe.objects.filter(user_id=userprofile.user_id)
    # for recipes in other_recips:
    #     if recipes.id == id:
    #         other_recips.remove()

    ingredients_list = recipe.ingredients.split(',')
    nutritions_list = recipe.nutrition.split(',')
    context = {
        'recipe': recipe,
        'ingredients': ingredients_list,
        'nutritions': nutritions_list,
        'userprofile': userprofile,
        'other_recipes_by_user': other_recips,
    }
    return render(request, 'recipe/user_recipe_detail.html', context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            recipes = Recipes.objects.order_by('-rating').filter(Q(recipe_name__icontains=keyword) | Q(ingredients__icontains=keyword))
            recipes_count = recipes.count()

    paginator = Paginator(recipes,15)
    page = request.GET.get('page')
    paged_recipes = paginator.get_page(page)
    context={
        'recipes': paged_recipes,
        'recipes_count': recipes_count,
        'keyword': keyword,
    }
    return render(request, 'recipe/all_recipes.html', context)