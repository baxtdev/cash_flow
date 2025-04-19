from django.contrib import admin

from .models import (
    Status,Type,Category,
    Subcategory,Record
)

#inlines 
class CategoryInline(admin.TabularInline):
    model = Category
    extra = 0


class SubcategoryInline(admin.TabularInline):
    model = Subcategory
    extra = 0



@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    inlines = [CategoryInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','type']
    search_fields = ['name']
    list_filter = ['type']
    inlines = [SubcategoryInline]


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['name','category']
    search_fields = ['name']
    list_filter = ['category','category__type']


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ['created_date','status','type','category','subcategory','amount','comment']
    list_filter = ['status','type','category','subcategory','created_date']

