# Generated by Django 5.0.6 on 2024-08-08 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_alter_buyer_product_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='product_image',
            field=models.ImageField(upload_to='static/buyer/'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_Photo',
            field=models.ImageField(upload_to='static/prod_img/'),
        ),
    ]
