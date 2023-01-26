# Generated by Django 4.1.5 on 2023-01-25 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=1)),
                ('data', models.DateField()),
                ('valor', models.IntegerField()),
                ('CPF', models.CharField(max_length=11)),
                ('cartao', models.CharField(max_length=12)),
                ('hora', models.CharField(max_length=6)),
                ('dono_da_loja', models.CharField(max_length=14)),
                ('nome_da_loja', models.CharField(max_length=19)),
            ],
        ),
    ]
