# Generated by Django 4.2.5 on 2023-09-15 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0026_tarea_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='correo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='notas',
            field=models.TextField(blank=True, null=True),
        ),
    ]