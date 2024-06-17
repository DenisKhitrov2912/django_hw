from django.core.management import BaseCommand

from catalog.models import Category, Product

import json


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('data.json') as file:
            data = json.load(file)
            return data

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()

        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(**category['fields'])
            )

            # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        product_for_create = [
            {'name': 'Samsung 3000', 'description': 'sampletext', 'image': '', 'category': category_for_create[0],
             'cost': '1000', 'created_at': '2023-01-21', 'updated_at': '2023-01-22'},
            {'name': 'Sony 3000', 'description': 'sample_text', 'image': '', 'category': category_for_create[0],
             'cost': '1060', 'created_at': '2023-02-21', 'updated_at': '2023-02-22'},
            {'name': 'JVC 1', 'description': 'samptext', 'image': '', 'category': category_for_create[1],
             'cost': '6500',
             'created_at': '2023-03-21', 'updated_at': '2023-03-22'},
            {'name': 'HP', 'description': 'sample text', 'image': '', 'category': category_for_create[2],
             'cost': '4000',
             'created_at': '2023-04-21', 'updated_at': '2023-04-22'}
        ]

        for products_item in product_for_create:
            Product.objects.create(**products_item)
