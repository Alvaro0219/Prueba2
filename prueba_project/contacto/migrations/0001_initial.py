# Generated by Django 4.1.4 on 2022-12-29 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(blank=True, max_length=100, verbose_name='Apellido')),
                ('correo', models.CharField(blank=True, max_length=100, verbose_name='Correo')),
                ('edad', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contactos',
                'ordering': ['nombre'],
            },
        ),
    ]
