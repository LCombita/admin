# Generated by Django 3.2 on 2022-03-20 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stage', '0010_repartoetapa_tipo_repartoetapa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repartoetapa',
            name='tipo_repartoetapa',
            field=models.CharField(choices=[('G', 'GENERAL'), ('I', 'IMPUESTO'), ('R', 'REVISION')], default='G', max_length=1),
        ),
        migrations.AlterField(
            model_name='revision',
            name='descripcion',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='revision',
            name='fecha_revision',
            field=models.DateField(verbose_name='Fecha Final'),
        ),
        migrations.AlterField(
            model_name='revision',
            name='reproceso',
            field=models.BooleanField(default=False),
        ),
    ]
