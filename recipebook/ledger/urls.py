from django.urls import path, include
from .views import *

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name='recipe_list'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/add', RecipeCreateView.as_view(), name='recipe_add'),
    path('recipe/<int:pk>/add_image', recipe_image_add, name='recipe_image_add'),
]

app_name = "ledger"