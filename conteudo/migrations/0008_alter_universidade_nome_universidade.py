# Generated by Django 4.1.2 on 2022-10-28 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conteudo', '0007_alter_universidade_cultura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='universidade',
            name='nome_universidade',
            field=models.CharField(max_length=255),
        ),
    ]
