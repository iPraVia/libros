# Generated by Django 4.1.2 on 2022-11-30 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_remove_libro_description_remove_libro_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='descripcion',
            field=models.CharField(default='', max_length=150),
        ),
    ]
