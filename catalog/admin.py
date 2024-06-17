from django.contrib import admin

from catalog.models import Category, Product, Contacts


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cost', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Contacts)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email',)
    search_fields = ('name', 'phone', 'email',)
