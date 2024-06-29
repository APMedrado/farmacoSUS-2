from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import Farmaco, EstoqueLocal, EstoqueRegional, LowStockAlert, Paciente, Medico, PostoDistribuicao, RegistroEntrega

# Serializers: Úteis para converter entre JSON e objeto do banco de dados

class FarmacoSerializer(DocumentSerializer):
    class Meta:
        model = Farmaco
        fields = '__all__'
        extra_kwargs = {
            'codigo_barra': {'read_only': False}
        }

class PostoDistribuicaoSerializer(DocumentSerializer):
    class Meta:
        model = PostoDistribuicao
        fields = '__all__'
        extra_kwargs = {
            'cnes': {'read_only': False}
        }

class EstoqueLocalCreateSerializer(DocumentSerializer):
    class Meta:
        model = EstoqueLocal
        fields = '__all__'
        extra_kwargs = {
            'medicamento': {'required': True},
            'posto_distribuicao': {'required': True}
        }

class EstoqueLocalSerializer(DocumentSerializer):
    medicamento = FarmacoSerializer()
    posto_distribuicao = PostoDistribuicaoSerializer()

    class Meta:
        model = EstoqueLocal
        fields = '__all__'

class EstoqueRegionalCreateSerializer(DocumentSerializer):
    class Meta:
        model = EstoqueRegional
        fields = '__all__'
        extra_kwargs = {
            'medicamento': {'required': True}
        }

class EstoqueRegionalSerializer(DocumentSerializer):
    medicamento = FarmacoSerializer()
    
    class Meta:
        model = EstoqueRegional
        fields = '__all__'
        extra_kwargs = {
            'medicamento': {'read_only': False}
        }

class PacienteSerializer(DocumentSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'
        extra_kwargs = {
            'cpf': {'read_only': False}
        }

class MedicoSerializer(DocumentSerializer):
    class Meta:
        model = Medico
        fields = '__all__'
        extra_kwargs = {
            'crm': {'read_only': False}
        }

class MedicamentoEntregaSerializer(serializers.Serializer):
    codigo_barra = serializers.CharField()
    quantidade = serializers.IntegerField()
    produto = serializers.SerializerMethodField()

    def get_produto(self, obj):
        try:
            medicamento = Farmaco.objects.get(codigo_barra=obj['codigo_barra'])
            return medicamento.produto
        except Farmaco.DoesNotExist:
            return None

class RegistroEntregaSerializer(DocumentSerializer):
    beneficiario = PacienteSerializer()
    receita_medico = MedicoSerializer()
    posto_distribuicao = PostoDistribuicaoSerializer()
    medicamentos = MedicamentoEntregaSerializer(many=True)

    class Meta:
        model = RegistroEntrega
        fields = '__all__'

class RegistroEntregaCreateSerializer(DocumentSerializer):
    class Meta:
        model = RegistroEntrega
        fields = '__all__'
        
class LowStockAlertSerializer(serializers.ModelSerializer):
    medicamento = FarmacoSerializer()
    posto_distribuicao = PostoDistribuicaoSerializer()

    class Meta:
        model = LowStockAlert
        fields = '__all__'