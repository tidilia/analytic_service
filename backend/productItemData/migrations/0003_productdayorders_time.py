# Generated by Django 5.0.6 on 2024-06-04 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productItemData', '0002_alter_productdayorders_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdayorders',
            name='time',
            field=models.IntegerField(default=None),
        ),
    ]
