# Generated by Django 4.2.5 on 2023-09-11 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_tecnico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='firma',
            field=models.ImageField(blank=True, null=True, upload_to='firmas'),
        ),
    ]
