# Generated by Django 4.2.5 on 2023-09-12 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0020_alter_tarea_estatus_pago'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='notas_tecnico',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='description',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='status',
            field=models.IntegerField(choices=[(1, 'Pendiente'), (2, 'Completada'), (3, 'cancelada')], default=1),
        ),
    ]
