# Generated by Django 5.0.6 on 2024-06-04 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productItemData', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdayorders',
            name='date',
            field=models.DateTimeField(default=None),
        ),
    ]