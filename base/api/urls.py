
# base/api/urls.py
from django.urls import path
from . import views  # Ensure views are imported correctly

urlpatterns = [
    # Example of a valid URL pattern
    path('example/', views.example_view, name='example'),
]
