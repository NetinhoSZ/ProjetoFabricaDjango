# Generated by Django 4.1.1 on 2022-09-17 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0006_rename_observacoes_mensalidade_treino'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensalidade',
            name='data',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
