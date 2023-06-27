# Generated by Django 4.2.1 on 2023-06-26 18:18

import apps.galeria.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import functools


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Arte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Envio de arte', (('AGUARDANDO', 'Aguardando'), ('ENVIADO', 'Enviado'), ('APROVADO', 'Aprovado'))), ('Confecção', (('AGUARDANDO', 'Aguardando'), ('EM_ANDAMENTO', 'Em andamento'), ('CONCLUÍDO', 'Concluído'))), ('Aprovação', (('AGUARDANDO', 'Aguardando'), ('ALTERAÇÃO', 'Alteração'), ('APROVADA', 'Aprovada')))], default='ENVIO-AGUARDANDO', max_length=100)),
                ('idCustomer', models.IntegerField()),
                ('idOrder', models.IntegerField()),
                ('idProduct', models.IntegerField()),
                ('instructions', models.CharField(max_length=500)),
                ('referencefiles', models.FileField(blank=True, upload_to=functools.partial(apps.galeria.models.upload_file_path, *(), **{'field_name': 'references'}))),
                ('mockup', models.ImageField(blank=True, upload_to=functools.partial(apps.galeria.models.upload_file_path, *(), **{'field_name': 'mockup'}))),
                ('alteracoes', models.CharField(max_length=500)),
                ('alterafiles', models.ImageField(blank=True, upload_to=functools.partial(apps.galeria.models.upload_file_path, *(), **{'field_name': 'alterafiles'}))),
                ('alteracounter', models.PositiveIntegerField(default=0)),
                ('artefinal', models.ImageField(blank=True, upload_to=functools.partial(apps.galeria.models.upload_file_path, *(), **{'field_name': 'artefinal'}))),
            ],
        ),
        migrations.CreateModel(
            name='Fotografia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('legenda', models.CharField(max_length=150)),
                ('categoria', models.CharField(choices=[('BRIEFING', 'Briefing'), ('REVISÃO', 'Revisão'), ('CONFECÇÃO', 'Confecção'), ('ALTERAÇÃO', 'Alteração'), ('APROVAÇÃO', 'Aprovação'), ('APROVADA', 'Aprovada')], default='', max_length=100)),
                ('descricao', models.TextField()),
                ('foto', models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d/')),
                ('publicada', models.BooleanField(default=True)),
                ('data_fotografia', models.DateTimeField(default=datetime.datetime.now)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
