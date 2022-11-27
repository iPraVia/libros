# Generated by Django 4.1.2 on 2022-11-27 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('rut', models.CharField(max_length=9)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=10)),
                ('estado', models.BooleanField()),
                ('tipoUsuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.tipousuario')),
            ],
        ),
    ]