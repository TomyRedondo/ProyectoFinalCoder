# Generated by Django 5.0.1 on 2024-01-25 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_delete_anime_alter_videojuego_autor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videojuego',
            name='autor',
        ),
        migrations.AddField(
            model_name='videojuego',
            name='fecha',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
    ]