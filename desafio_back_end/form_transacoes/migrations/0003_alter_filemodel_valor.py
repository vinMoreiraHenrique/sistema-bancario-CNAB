# Generated by Django 4.1.5 on 2023-01-25 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_transacoes', '0002_remove_filemodel_cpf_alter_filemodel_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemodel',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]
