# Generated by Django 4.2.5 on 2023-09-12 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0018_tarea_porcentaje_de_pago_alter_tarea_estatus_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='porcentaje_de_pago',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
