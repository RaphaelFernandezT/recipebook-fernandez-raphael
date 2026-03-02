from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('ledger:recipe_list', args=[str(self.pk)])

class Recipe(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('ledger:recipe_detail', args=[str(self.pk)])
    

class RecipeIngredient(models.Model):
    quantity = models.DecimalField(max_digits=100,decimal_places=0 )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='recipe'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients'
    )

