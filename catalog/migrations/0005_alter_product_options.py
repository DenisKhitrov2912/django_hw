# Generated by Django 4.2 on 2024-03-25 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': [('set_published', 'Can publish products')], 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
    ]
