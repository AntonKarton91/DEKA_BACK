# Generated by Django 4.1.1 on 2022-10-17 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablecolumns',
            name='order',
            field=models.CharField(default=[], max_length=255),
        ),
    ]