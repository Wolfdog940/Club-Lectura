# Generated by Django 5.1.7 on 2025-03-22 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_detalle_usuario_libros_grupo'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalle_usuario',
            name='accepta_notificaciones',
            field=models.BooleanField(default=True),
        ),
    ]
