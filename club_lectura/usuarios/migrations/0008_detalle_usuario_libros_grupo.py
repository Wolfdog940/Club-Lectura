# Generated by Django 5.1.7 on 2025-03-21 18:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0002_estado_libro_libro_usuario_resena_libro_grupo'),
        ('usuarios', '0007_detalle_usuario_generos'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='detalle_usuario',
            name='libros',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='libros_usuario', to='libros.libro_usuario'),
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('imagen_grupo', models.TextField(blank=True, null=True)),
                ('descripcion', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('administrador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grupo_administrador', to=settings.AUTH_USER_MODEL)),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grupo_libros', to='libros.libro_grupo')),
                ('miembros', models.ManyToManyField(related_name='grupo_miembros', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Grupo',
                'verbose_name_plural': 'Grupos',
            },
        ),
    ]
