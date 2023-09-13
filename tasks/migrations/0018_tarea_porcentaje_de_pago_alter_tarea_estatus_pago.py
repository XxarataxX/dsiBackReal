# Generated by Django 4.2.5 on 2023-09-12 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0017_alter_tarea_estatus_pago'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='porcentaje_de_pago',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tarea',
            name='estatus_pago',
            field=models.IntegerField(choices=[(1, 'Pendiente'), (2, 'Completada'), (3, 'cancelada')], default=1),
        ),
    ]
