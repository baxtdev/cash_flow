from django.urls import path
from . import views

urlpatterns = [
    path('ajax/load-categories/', views.load_categories, name='ajax_load_categories'),
    path('ajax/load-subcategories/', views.load_subcategories, name='ajax_load_subcategories'),
]
