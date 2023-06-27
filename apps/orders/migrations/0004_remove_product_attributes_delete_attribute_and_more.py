# Generated by Django 4.2.1 on 2023-06-26 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_remove_orderproduct_order_remove_product_artes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='attributes',
        ),
        migrations.DeleteModel(
            name='Attribute',
        ),
        migrations.AddField(
            model_name='product',
            name='attributes',
            field=models.JSONField(null=True),
        ),
    ]
