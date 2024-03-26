from django.conf import settings
from django.core.cache import cache

from catalog.models import Category


def get_categories():
    categories = Category.objects.all()
    if settings.CACHE_ENABLED:
        key = 'category_list'
        category_list = cache.get(key)
        #print(category_list)#для проверки кеша
        if category_list is None:
            category_list = categories
            cache.set(key, category_list)
    else:
        category_list = categories
    context = {
        'category_list': category_list
    }

    return context
