from django import forms

from .models import *

class RecipeForm(forms.Form):
    recipe_name = forms.CharField(label='Task Name', max_length=100)