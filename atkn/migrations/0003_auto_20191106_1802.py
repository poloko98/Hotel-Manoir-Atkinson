# Generated by Django 2.2.4 on 2019-11-06 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atkn', '0002_recepcionista'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recepcionista',
            options={'permissions': (('administrador', 'Es administrador'), ('recepcionista', 'Es recepcionista'))},
        ),
    ]
