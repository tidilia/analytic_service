# Generated by Django 5.0.6 on 2024-05-22 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='seoProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nmID', models.IntegerField(default=None)),
                ('name', models.CharField(default=None, max_length=100)),
                ('amount', models.IntegerField(default=None)),
                ('description', models.TextField(default=None, max_length=5000)),
            ],
        ),
    ]
