# Generated by Django 4.2 on 2024-03-25 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': [('set_published', 'Возможность изменить публикацию продукта')], 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
    ]
