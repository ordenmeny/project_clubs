# Generated by Django 4.2.13 on 2024-07-16 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_usermodel_telegram_verif_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='skills',
            field=models.TextField(blank=True, null=True, verbose_name='Навыки'),
        ),
    ]
