# Generated by Django 5.0.6 on 2024-07-15 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('verdoapp', '0003_rename_email_user_correo_remove_user_direccion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='activo',
        ),
    ]
