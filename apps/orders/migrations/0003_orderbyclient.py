# Generated by Django 4.2.2 on 2023-06-20 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_data_order_address_order_agency_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderByClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
