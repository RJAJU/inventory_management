# Generated by Django 2.2 on 2021-07-31 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventory',
            options={'verbose_name_plural': 'Inventory'},
        ),
        migrations.AlterField(
            model_name='member',
            name='date_joined',
            field=models.DateTimeField(),
        ),
    ]
