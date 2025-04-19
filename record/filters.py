from django.contrib import admin
from .models import Type, Category, Subcategory, Status

class TypeFilter(admin.SimpleListFilter):
    title = 'Тип'
    parameter_name = 'type'

    def lookups(self, request, model_admin):
        return [(t.id, t.name) for t in Type.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(type__id=self.value())
        return queryset


class CategoryFilter(admin.SimpleListFilter):
    title = 'Категория'
    parameter_name = 'category'

    def lookups(self, request, model_admin):
        return [(c.id, c.name) for c in Category.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(category__id=self.value())
        return queryset


class SubcategoryFilter(admin.SimpleListFilter):
    title = 'Подкатегория'
    parameter_name = 'subcategory'

    def lookups(self, request, model_admin):
        return [(s.id, s.name) for s in Subcategory.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(subcategory__id=self.value())
        return queryset


class StatusFilter(admin.SimpleListFilter):
    title = 'Статус'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [(s.id, s.name) for s in Status.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(status__id=self.value())
        return queryset
