# Generated by Django 4.1.2 on 2022-11-30 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_rename_texto_libro_descripcion_libro_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.usuario'),
        ),
    ]
