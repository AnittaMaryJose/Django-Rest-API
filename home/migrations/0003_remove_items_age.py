# Generated by Django 4.2.7 on 2023-12-19 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_items_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='age',
        ),
    ]
