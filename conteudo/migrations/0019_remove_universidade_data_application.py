# Generated by Django 4.1.2 on 2022-11-02 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conteudo', '0018_pais_clima_pais_descricao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='universidade',
            name='data_application',
        ),
    ]
