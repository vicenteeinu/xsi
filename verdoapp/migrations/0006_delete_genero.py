# Generated by Django 5.0.6 on 2024-07-15 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('verdoapp', '0005_remove_user_id_genero'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Genero',
        ),
    ]
