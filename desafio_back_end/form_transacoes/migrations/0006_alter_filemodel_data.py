# Generated by Django 4.1.5 on 2023-01-26 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_transacoes', '0005_alter_filemodel_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemodel',
            name='data',
            field=models.DateField(),
        ),
    ]