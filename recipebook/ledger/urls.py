from django.urls import path
from .views import homepage, recipelist

urlpatterns = [
    path('', homepage, name='homepage'),
    path('list', recipelist, name='recipelist'),
]

app_name = "ledger"