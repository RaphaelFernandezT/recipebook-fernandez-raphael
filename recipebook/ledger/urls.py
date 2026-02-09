from django.urls import path
from .views import homepage, recipelist, recipe1, recipe2

urlpatterns = [
    path('', homepage, name='homepage'),
    path('recipes/list', recipelist, name='recipelist'),
    path('1', recipe1, name='recipe1'),
    path('2', recipe2, name='recipe2'),
]

app_name = "ledger"