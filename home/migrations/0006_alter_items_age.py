# Generated by Django 4.2.7 on 2023-12-19 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_items_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='age',
            field=models.IntegerField(),
        ),
    ]