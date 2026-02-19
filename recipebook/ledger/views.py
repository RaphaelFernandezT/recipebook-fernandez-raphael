from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe

class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipelist.html'
    context_object_name = 'ingredients' 

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'ledger/recipedetail.html'
    context_object_name = 'recipe'
