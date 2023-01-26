from django.db import models

class FileModel(models.Model):
    tipo = models.CharField(max_length=1)
    data = models.DateField()
    valor = models.DecimalField(decimal_places=2, max_digits=20)
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=12)
    hora = models.TimeField(max_length=6)
    dono_da_loja = models.CharField(max_length=14)
    nome_da_loja = models.CharField(max_length=19)
