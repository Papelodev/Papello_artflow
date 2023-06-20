# Generated by Django 4.2.1 on 2023-06-20 14:14

import apps.galeria.models
from django.db import migrations, models
import functools
from apps.galeria.models import upload_file_path



class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0009_alter_fotografia_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Envio de arte', (('AGUARDANDO', 'Aguardando'), ('ENVIADO', 'Enviado'), ('APROVADO', 'Aprovado'))), ('Confecção', (('AGUARDANDO', 'Aguardando'), ('EM_ANDAMENTO', 'Em andamento'), ('CONCLUÍDO', 'Concluído'))), ('Aprovação', (('AGUARDANDO', 'Aguardando'), ('ALTERAÇÃO', 'Alteração'), ('APROVADA', 'Aprovada')))], default='ENVIO-AGUARDANDO', max_length=100)),
                ('idCustomer', models.IntegerField()),
                ('idOrder', models.IntegerField()),
                ('instructions', models.CharField(max_length=500)),
                ('referencefiles', models.FileField(blank=True, upload_to=functools.partial(apps.galeria.models.upload_file_path, *(), **{'field_name': 'references'}))),
                ('mockup', models.ImageField(blank=True, upload_to=functools.partial(apps.galeria.models.upload_file_path, *(), **{'field_name': 'mockup'}))),
                ('alteracoes', models.CharField(max_length=500)),
                ('alterafiles', models.ImageField(blank=True, upload_to=functools.partial(apps.galeria.models.upload_file_path, *(), **{'field_name': 'alterafiles'}))),
                ('alteracounter', models.PositiveIntegerField(default=0)),
                ('artefinal', models.ImageField(blank=True, upload_to=functools.partial(apps.galeria.models.upload_file_path, *(), **{'field_name': 'artefinal'}))),
            ],
        ),
    ]
