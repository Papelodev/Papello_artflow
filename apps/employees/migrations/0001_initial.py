# Generated by Django 4.2.1 on 2023-06-20 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=100)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.myuser')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.CharField(max_length=50)),
                ('due_date', models.DateField()),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employees.employeeprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField()),
                ('rating', models.PositiveIntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('reviewer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='employees.employeeprofile')),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employees.task')),
            ],
        ),
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='designs/')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('designer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='designs', to='employees.employeeprofile')),
            ],
        ),
    ]
