from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import *
from .models import *

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'ledger/recipe_list.html'
    context_object_name = 'recipes' 

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'ledger/recipe_detail.html'
    context_object_name = 'recipe'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm

    def form_invalid(self, form):
        form.instance.profile = Profile.objects.get(user=self.request.user)
        return super().form_invalid(form)
    
def recipe_image_add(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            recipeImage = form.save(commit=False)
            recipeImage.recipe = recipe
            recipeImage.save()
            return redirect('ledger:recipe_detail')
    else:
        form = RecipeImageForm()
        return render(request, 'ledger/recipeimage_form.html', {'form': form})
