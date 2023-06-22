# Generated by Django 4.2.1 on 2023-06-22 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_order_idqueue'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='product_name',
        ),
        migrations.AddField(
            model_name='product',
            name='idOrderItem',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
