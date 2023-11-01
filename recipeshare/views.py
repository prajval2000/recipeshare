from django.http import HttpResponse
from django.shortcuts import render
from recipes.models import Recipes
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def home(request):
    recipes = Recipes.objects.all()
    paginator = Paginator(recipes,15)
    page = request.GET.get('page')
    paged_recipes = paginator.get_page(page)
    context={
        'recipes' : paged_recipes
    }
    return render(request, 'home.html', context)