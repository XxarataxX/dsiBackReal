# Generated by Django 4.2.5 on 2023-09-13 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0021_tarea_notas_tecnico_alter_tarea_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historial_pagos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pago_porcentaje', models.IntegerField(blank=True, null=True)),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.tarea')),
            ],
        ),
    ]