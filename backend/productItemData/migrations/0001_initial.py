# Generated by Django 5.0.6 on 2024-06-03 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='productDayOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=None)),
                ('nmID', models.IntegerField(default=None)),
                ('sku', models.CharField(default=None, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='productWeekOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=None)),
                ('nmID', models.IntegerField(default=None)),
                ('sku', models.CharField(default=None, max_length=30)),
            ],
        ),
    ]
