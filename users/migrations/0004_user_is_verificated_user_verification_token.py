# Generated by Django 4.2 on 2024-03-24 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_delete_emailverificationtoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_verificated',
            field=models.BooleanField(default=False, verbose_name='верификация'),
        ),
        migrations.AddField(
            model_name='user',
            name='verification_token',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='токен верификации'),
        ),
    ]