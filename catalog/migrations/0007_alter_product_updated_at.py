# Generated by Django 5.0.2 on 2024-02-23 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_blogwriting_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='дата изменения'),
        ),
    ]