# Generated by Django 4.2.2 on 2023-06-27 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_myuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'customer'), (2, 'admin'), (3, 'designer'), (4, 'reviewer'), (5, 'employee')], null=True),
        ),
    ]