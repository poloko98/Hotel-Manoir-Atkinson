# Generated by Django 2.2.4 on 2019-11-17 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atkn', '0003_auto_20191106_1802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Recepcionista',
        ),
        migrations.AlterModelOptions(
            name='reserva',
            options={'permissions': (('administrador', 'Es administrador'), ('recepcionista', 'Es recepcionista'))},
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
