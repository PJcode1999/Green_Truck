# Generated by Django 4.1.7 on 2023-08-17 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.FloatField(default=10.89, max_length=10),
        ),
    ]
