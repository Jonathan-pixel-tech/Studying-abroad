# Generated by Django 4.1.2 on 2022-11-02 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conteudo', '0017_rename_application_universidade_descricao_application_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pais',
            name='clima',
            field=models.TextField(default='A nice country'),
        ),
        migrations.AddField(
            model_name='pais',
            name='descricao',
            field=models.TextField(default='A nice country'),
        ),
    ]
