# Generated by Django 4.1.7 on 2023-08-21 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_product_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cat_photo',
            field=models.ImageField(default=1, upload_to='category'),
            preserve_default=False,
        ),
    ]