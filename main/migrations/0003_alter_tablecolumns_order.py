# Generated by Django 4.1.1 on 2022-10-18 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_tablecolumns_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablecolumns',
            name='order',
            field=models.CharField(default='', max_length=255),
        ),
    ]
