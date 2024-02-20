from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='имя')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        print(f"{self.name}")

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='имя')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='превью', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cost = models.IntegerField(verbose_name='цена')
    created_at = models.DateField(verbose_name='дата создания')
    updated_at = models.DateField(verbose_name='дата изменения')

    def __str__(self):
        print(f"{self.name}, {self.cost}")

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
