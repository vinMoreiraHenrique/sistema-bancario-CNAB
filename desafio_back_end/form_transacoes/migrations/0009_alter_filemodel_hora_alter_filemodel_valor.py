# Generated by Django 4.1.5 on 2023-01-26 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_transacoes', '0008_alter_filemodel_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemodel',
            name='hora',
            field=models.TimeField(max_length=6),
        ),
        migrations.AlterField(
            model_name='filemodel',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]