# Generated by Django 4.1.2 on 2022-10-28 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conteudo', '0005_alter_pais_continente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='universidade',
            name='application',
            field=models.TextField(),
        ),
    ]