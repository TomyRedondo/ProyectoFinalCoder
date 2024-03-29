# Generated by Django 5.0.1 on 2024-01-22 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_manga_novela_videojuego_rename_apellido_anime_autor_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Novela',
        ),
        migrations.AlterModelOptions(
            name='anime',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterModelOptions(
            name='manga',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterModelOptions(
            name='videojuego',
            options={'ordering': ['nombre']},
        ),
        migrations.RenameField(
            model_name='anime',
            old_name='autor',
            new_name='seudonimo',
        ),
        migrations.RenameField(
            model_name='manga',
            old_name='autor',
            new_name='seudonimo',
        ),
    ]
