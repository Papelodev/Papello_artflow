# Generated by Django 4.2.1 on 2023-07-04 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_alter_orderproduct_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='artes',
        ),
    ]
