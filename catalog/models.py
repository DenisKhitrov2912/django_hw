from django.db import models
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='имя')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='имя')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='catalog/', verbose_name='превью', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    cost = models.IntegerField(verbose_name='цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата изменения', **NULLABLE)

    def __str__(self):
        return f"{self.name}, {self.description}, {self.image}, {self.category}, {self.cost}, {self.created_at}, {self.updated_at}"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(Product, self).save(*args, **kwargs)

    def active_version(self):
        return self.version_set.filter(is_current=True).first()


class Contacts(models.Model):
    name = models.CharField(max_length=200, verbose_name='имя')
    phone = models.IntegerField(verbose_name='телефон')
    email = models.EmailField(verbose_name='email')

    def __str__(self):
        return f"{self.name}, {self.phone}, {self.email}"

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


class BlogWriting(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=100, verbose_name='slug', **NULLABLE)
    context = models.TextField(verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='catalog/', verbose_name='превью', **NULLABLE)
    created_at = models.DateField(auto_now_add=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    count_of_views = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f"{self.title}, {self.context}, {self.created_at}"

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.CharField(max_length=50, verbose_name='номер версии')
    version_name = models.CharField(max_length=200, verbose_name='название версии')
    is_current = models.BooleanField(default=False, verbose_name='признак текущей версии')

    def __str__(self):
        return f"{self.product.name} - {self.version_number}"

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'