# Generated by Django 4.2.2 on 2023-07-11 17:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('galeria', '0007_arte_designer_responsible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arte',
            name='designer_responsible',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Arte', to=settings.AUTH_USER_MODEL),
        ),
    ]