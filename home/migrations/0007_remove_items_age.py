# Generated by Django 4.2.7 on 2023-12-19 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_items_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='age',
        ),
    ]