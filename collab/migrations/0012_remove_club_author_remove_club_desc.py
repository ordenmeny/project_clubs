# Generated by Django 4.2.14 on 2024-08-19 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collab', '0011_club'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='author',
        ),
        migrations.RemoveField(
            model_name='club',
            name='desc',
        ),
    ]