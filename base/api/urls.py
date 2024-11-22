# base/api/urls.py
from django.urls import path
from . import views  # Make sure views is imported correctly

urlpatterns = [
    path('example/', views.example_view, name='example'),
]
