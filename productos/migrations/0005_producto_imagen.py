# Generated by Django 4.2.13 on 2024-06-29 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_elimina_modelo_productos'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default='media/default.png', upload_to='productos/'),
        ),
    ]
