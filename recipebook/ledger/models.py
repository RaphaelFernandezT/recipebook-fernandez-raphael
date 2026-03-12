from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True) 
    bio = models.TextField(blank=True)

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('ledger:recipe_list', args=[str(self.pk)])

class Recipe(models.Model):
    name = models.CharField(max_length=100)    
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='recipes', null=True, blank=True)  
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)  
    updated_on = models.DateTimeField(auto_now=True, null=True, blank=True)  


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

class RecipeImage(models.Model):
    image = models.ImageField(upload_to='images/', null=True)
    description = models.CharField(max_length=255)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='image'
    )
