# Generated by Django 4.2 on 2024-03-25 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_product_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_published',
        ),
    ]