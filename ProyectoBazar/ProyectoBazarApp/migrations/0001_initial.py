# Generated by Django 4.0.5 on 2022-06-23 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=30, verbose_name='Artículo')),
                ('detalle', models.CharField(max_length=30, verbose_name='Detalle')),
                ('cantidad', models.PositiveIntegerField(verbose_name='Cantidad')),
                ('color', models.CharField(max_length=15, verbose_name='Color')),
                ('precio', models.FloatField(verbose_name='Precio $')),
            ],
        ),
    ]
