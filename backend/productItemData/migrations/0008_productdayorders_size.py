# Generated by Django 5.0.6 on 2024-06-05 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productItemData', '0007_productweekorders_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdayorders',
            name='size',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
