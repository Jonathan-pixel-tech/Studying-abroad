# Generated by Django 4.1.2 on 2022-10-28 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conteudo', '0006_alter_universidade_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='universidade',
            name='cultura',
            field=models.TextField(blank=True, null=True),
        ),
    ]