# Generated by Django 4.2.2 on 2023-06-23 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0010_alter_artes_idcustomer'),
    ]

    operations = [
        migrations.AddField(
            model_name='artes',
            name='idOrder',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='artes',
            name='idCustomer',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
