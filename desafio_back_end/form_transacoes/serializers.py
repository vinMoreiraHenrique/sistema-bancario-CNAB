from django.core import serializers

class FileModelSerializer(serializers.Serializer):
    tipo = serializers.CharField()
    data = serializers.DateField()
    valor = serializers.DecimalField(decimal_places=2, max_digits=20)
    cpf = serializers.CharField()
    cartao = serializers.CharField()
    hora = serializers.TimeField()
    dono_da_loja = serializers.CharField()
    nome_da_loja = serializers.CharField()
    total_saldo = serializers.DecimalField(decimal_places=2, max_digits=20)
   
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['total_saldo'] = "{:.2f}".format(representation['total_saldo'])
        return representation