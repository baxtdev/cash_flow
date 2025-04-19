from django import forms
from .models import Record, Category, Subcategory

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Изначально блокируем поля
        self.fields['category'].queryset = Category.objects.none()
        self.fields['subcategory'].queryset = Subcategory.objects.none()

        if 'type' in self.data:
            try:
                type_id = int(self.data.get('type'))
                self.fields['category'].queryset = Category.objects.filter(type_id=type_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['category'].queryset = Category.objects.filter(type=self.instance.type)

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = Subcategory.objects.filter(category_id=category_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['subcategory'].queryset = Subcategory.objects.filter(category=self.instance.category)
