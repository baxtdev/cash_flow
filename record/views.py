from django.shortcuts import render

from django.http import JsonResponse
from .models import Category, Subcategory

def load_categories(request):
    print("request type")
    type_id = request.GET.get('type')
    categories = Category.objects.filter(type_id=type_id).order_by('name')
    return JsonResponse(list(categories.values('id', 'name')), safe=False)

def load_subcategories(request):
    print("request categriy")
    category_id = request.GET.get('category')
    subcategories = Subcategory.objects.filter(category_id=category_id).order_by('name')
    return JsonResponse(list(subcategories.values('id', 'name')), safe=False)
