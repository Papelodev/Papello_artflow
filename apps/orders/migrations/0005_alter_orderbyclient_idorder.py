# Generated by Django 4.2.2 on 2023-06-20 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_orderbyclient_document_orderbyclient_idorder_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderbyclient',
            name='idOrder',
            field=models.IntegerField(default=0),
        ),
    ]
