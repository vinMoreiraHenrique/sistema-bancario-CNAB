# Generated by Django 4.1.5 on 2023-01-25 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_transacoes', '0003_alter_filemodel_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemodel',
            name='valor',
            field=models.DecimalField(decimal_places=5, max_digits=20),
        ),
    ]
