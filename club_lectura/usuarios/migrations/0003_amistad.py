# Generated by Django 5.1.7 on 2025-03-09 19:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_remove_detalleusuario_bio'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Amistad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario_principal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amistades_principales', to=settings.AUTH_USER_MODEL)),
                ('usuario_secundario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amistades_secundarias', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('usuario_principal', 'usuario_secundario')},
            },
        ),
    ]
