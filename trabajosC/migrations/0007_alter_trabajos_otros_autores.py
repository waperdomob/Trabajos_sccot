# Generated by Django 4.0.4 on 2022-07-15 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabajosC', '0006_remove_trabajos_manuscritos_remove_trabajos_tablas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajos',
            name='otros_autores',
            field=models.ManyToManyField(blank=True, null=True, related_name='+', through='trabajosC.Trabajos_has_autores', to='trabajosC.autores'),
        ),
    ]