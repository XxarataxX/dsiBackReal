# Generated by Django 4.2.5 on 2023-09-11 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_rename_archivo_pdf_pdfgenerado_archivo'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdfgenerado',
            name='name',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
