# Generated by Django 4.2 on 2024-03-25 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_alter_blogwriting_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogwriting',
            options={'verbose_name': 'блог', 'verbose_name_plural': 'блоги'},
        ),
    ]
