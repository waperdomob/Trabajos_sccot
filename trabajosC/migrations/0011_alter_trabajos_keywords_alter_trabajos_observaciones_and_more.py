# Generated by Django 4.0.4 on 2022-07-22 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabajosC', '0010_alter_trabajos_institucion_principal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajos',
            name='keywords',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='trabajos',
            name='observaciones',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trabajos',
            name='palabras_claves',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='trabajos',
            name='resumen_esp',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='trabajos',
            name='resumen_ingles',
            field=models.TextField(),
        ),
    ]
