# Generated by Django 5.0.6 on 2024-05-22 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seo', '0002_remove_seoproduct_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='seoProduct',
        ),
    ]
