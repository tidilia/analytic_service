# Generated by Django 5.0.6 on 2024-06-18 09:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productItemData', '0008_productdayorders_size'),
        ('products', '0002_remove_goods_nmid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdayorders',
            name='nmID',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
        migrations.AlterField(
            model_name='productweekorders',
            name='nmID',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
