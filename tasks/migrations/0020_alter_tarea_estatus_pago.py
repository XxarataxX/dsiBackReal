# Generated by Django 4.2.5 on 2023-09-12 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0019_alter_tarea_porcentaje_de_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='estatus_pago',
            field=models.IntegerField(choices=[(1, 'no pagado'), (2, 'cobrado'), (3, 'cancelada')], default=1),
        ),
    ]