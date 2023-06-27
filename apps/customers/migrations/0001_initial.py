# Generated by Django 4.2.1 on 2023-06-26 18:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('idCustomer', models.IntegerField()),
                ('nameCustomer', models.CharField(max_length=255)),
                ('phone1', models.CharField(max_length=20)),
                ('phone2', models.CharField(max_length=20)),
                ('birthDate', models.DateField()),
                ('typeCustomer', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('billingAddress', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=10)),
                ('cpf_cnpj', models.CharField(max_length=20)),
                ('rg_ie', models.CharField(max_length=20)),
                ('customerExternalId', models.CharField(max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]