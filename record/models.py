from django.db import models



class Status(models.Model):
    name = models.CharField(
        verbose_name="Название Статуса",
        max_length=100, 
        unique=True
        )
    
    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
    
    def __str__(self):
        return self.name




class Type(models.Model):
    name = models.CharField(
        verbose_name="Название Типа",
        max_length=100, 
        unique=True
        )
    
    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def __str__(self):
        return self.name
    


class Category(models.Model):
    name = models.CharField(
        verbose_name="Название",
        max_length=100
        )
    type = models.ForeignKey(
        Type, 
        verbose_name="Тип",
        related_name='categories', 
        on_delete=models.CASCADE
        )

    class Meta:
        unique_together = ('name', 'type')
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.name} ({self.type.name})"


class Subcategory(models.Model):
    name = models.CharField(
        verbose_name="Название",
        max_length=100
        )
    category = models.ForeignKey(
        Category,
        verbose_name="Родительская категория",
        related_name='subcategories', 
        on_delete=models.CASCADE
        )

    class Meta:
        unique_together = ('name', 'category')
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"


    def __str__(self):
        return f"{self.name} ({self.category.name})"


class Record(models.Model):
    created_date = models.DateField(
        verbose_name="Дата создания",
        auto_now=True
    )
    status = models.ForeignKey(
        Status,
        verbose_name="Статус",
        on_delete=models.CASCADE,
        related_name="records"
    )
    type = models.ForeignKey(
        Type,
        verbose_name="Тип",
        on_delete=models.CASCADE,
        related_name="records"
    )
    category = models.ForeignKey(
        Category,
        verbose_name="Категория",
        on_delete=models.CASCADE,
        related_name="records"
    )
    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.CASCADE,
        verbose_name="Подкатегория",
        related_name="records"
    )
    amount = models.FloatField(
        verbose_name="Сумма"
    )
    comment = models.TextField(
        verbose_name="Комментарий",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'ДДС'
        verbose_name_plural = 'ДДС'
    
    def __str__(self):
        return f"{self.amount} ({self.type.name})"