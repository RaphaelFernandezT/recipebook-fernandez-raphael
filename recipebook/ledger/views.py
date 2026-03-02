from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe, Ingredient

class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipe_list.html'
    context_object_name = 'recipes' 

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'ledger/recipe_detail.html'
    pk_url_kwarg = 'id'
    context_object_name = 'recipe'
