from django.urls import path
from home.views import petros

urlpatterns = [
    path('', petros, name="petros")
]
