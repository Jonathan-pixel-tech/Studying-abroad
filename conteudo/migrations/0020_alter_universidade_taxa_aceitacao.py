# Generated by Django 4.1.2 on 2022-11-02 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conteudo', '0019_remove_universidade_data_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='universidade',
            name='taxa_aceitacao',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]
