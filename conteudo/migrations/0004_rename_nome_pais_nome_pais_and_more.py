# Generated by Django 4.1.2 on 2022-10-28 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conteudo', '0003_alter_pais_managers_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pais',
            old_name='nome',
            new_name='nome_pais',
        ),
        migrations.RenameField(
            model_name='universidade',
            old_name='nome',
            new_name='nome_universidade',
        ),
    ]
