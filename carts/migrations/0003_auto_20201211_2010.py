# Generated by Django 3.1.4 on 2020-12-11 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20201209_2022'),
        ('carts', '0002_cart_subtotal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, to='products.Product'),
        ),
    ]
