# Generated by Django 3.2 on 2022-03-17 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stage', '0004_alter_etapa_tipo_etapa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repartoetapa',
            name='fecha_final',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha Final'),
        ),
        migrations.AlterField(
            model_name='repartoetapa',
            name='fecha_inicio',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha Inicio'),
        ),
    ]
