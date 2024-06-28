from .kafka_producer import produce_message
from rest_framework_mongoengine import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Farmaco, EstoqueLocal, EstoqueRegional, Paciente, Medico, PostoDistribuicao, RegistroEntrega
from .serializers import FarmacoSerializer, EstoqueLocalSerializer, EstoqueRegionalSerializer, PacienteSerializer, MedicoSerializer, PostoDistribuicaoSerializer, RegistroEntregaCreateSerializer, RegistroEntregaSerializer
import logging
import json

logger = logging.getLogger(__name__)

# Views: Lidam com requests e responses. 'generics' gera CRUD básico

class FarmacoList(generics.ListCreateAPIView):
    queryset = Farmaco.objects.all()
    serializer_class = FarmacoSerializer

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            logger.info('Fármaco adicionado com sucesso: %s', response.data)
            return response
        except Exception as e:
            logger.error('Erro ao adicionar fármaco: %s', str(e))
            return Response({'detail': 'Erro ao adicionar fármaco'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class FarmacoDetail(generics.RetrieveAPIView):
    queryset = Farmaco.objects.all()
    serializer_class = FarmacoSerializer
    lookup_field = 'codigo_barra'

class EstoqueLocalList(generics.ListCreateAPIView):
    queryset = EstoqueLocal.objects.all()
    serializer_class = EstoqueLocalSerializer

@api_view(['POST'])
def CreateEstoqueLocalBatch(request):
    if isinstance(request.data, list):
        updated_entries = []
        for entry in request.data:
            medicamento_codigo = entry.get('medicamento')
            posto_cnes = entry.get('posto_distribuicao')
            quantidade = entry.get('quantidade')

            if not medicamento_codigo or not posto_cnes or not quantidade:
                return Response({"detail": "Missing data in request"}, status=status.HTTP_400_BAD_REQUEST)

            try:
                # Encontre o medicamento pelo código de barras
                medicamento = Farmaco.objects.get(codigo_barra=medicamento_codigo)
                
                # Encontre o posto de distribuição pelo CNES
                posto_distribuicao = PostoDistribuicao.objects.get(cnes=posto_cnes)
                
                # Verifique se existe uma entrada no estoque local para esse medicamento e posto de distribuição
                try:
                    estoque_local = EstoqueLocal.objects.get(medicamento=medicamento, posto_distribuicao=posto_distribuicao)
                    estoque_local.quantidade += quantidade
                    estoque_local.save()
                    updated_entries.append(estoque_local)
                except EstoqueLocal.DoesNotExist:
                    # Crie uma nova entrada no estoque local
                    estoque_local = EstoqueLocal(medicamento=medicamento, posto_distribuicao=posto_distribuicao, quantidade=quantidade)
                    estoque_local.save()
                    updated_entries.append(estoque_local)

            except Farmaco.DoesNotExist:
                return Response({"detail": "Medicamento não encontrado"}, status=status.HTTP_400_BAD_REQUEST)
            except PostoDistribuicao.DoesNotExist:
                return Response({"detail": "Posto de distribuição não encontrado"}, status=status.HTTP_400_BAD_REQUEST)

        response_serializer = EstoqueLocalSerializer(updated_entries, many=True)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
    return Response({"detail": "Invalid data format. Expected a list."}, status=status.HTTP_400_BAD_REQUEST)

class EstoqueRegionalList(generics.ListCreateAPIView):
    queryset = EstoqueRegional.objects.all()
    serializer_class = EstoqueRegionalSerializer

@api_view(['POST'])
def CreateEstoqueRegionalBatch(request):
    if isinstance(request.data, list):
        updated_entries = []
        for entry in request.data:
            medicamento_codigo = entry.get('medicamento')
            quantidade = entry.get('quantidade')

            if not medicamento_codigo or not quantidade:
                return Response({"detail": "Missing data in request"}, status=status.HTTP_400_BAD_REQUEST)

            try:
                # Encontre o medicamento pelo código de barras
                medicamento = Farmaco.objects.get(codigo_barra=medicamento_codigo)
                
                # Verifique se existe uma entrada no estoque regional para esse medicamento
                try:
                    estoque_regional = EstoqueRegional.objects.get(medicamento=medicamento)
                    estoque_regional.quantidade += quantidade  # Atualiza a quantidade
                    estoque_regional.save()  # Salva a entrada atualizada
                    updated_entries.append(estoque_regional)
                except EstoqueRegional.DoesNotExist:
                    # Crie uma nova entrada no estoque regional
                    estoque_regional = EstoqueRegional(medicamento=medicamento, quantidade=quantidade)
                    estoque_regional.save()
                    updated_entries.append(estoque_regional)

            except Farmaco.DoesNotExist:
                return Response({"detail": "Medicamento não encontrado"}, status=status.HTTP_400_BAD_REQUEST)

        response_serializer = EstoqueRegionalSerializer(updated_entries, many=True)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
    return Response({"detail": "Invalid data format. Expected a list."}, status=status.HTTP_400_BAD_REQUEST)

class PacienteList(generics.ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class PacienteDetail(generics.RetrieveAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    lookup_field = 'cpf'

class MedicoList(generics.ListCreateAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class MedicoDetail(generics.RetrieveAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    lookup_field = 'crm'

class PostoDistribuicaoList(generics.ListCreateAPIView):
    queryset = PostoDistribuicao.objects.all()
    serializer_class = PostoDistribuicaoSerializer

class PostoDistribuicaoDetail(generics.RetrieveAPIView):
    queryset = PostoDistribuicao.objects.all()
    serializer_class = PostoDistribuicaoSerializer
    lookup_field = 'cnes'

class RegistroEntregaListCreateView(generics.ListCreateAPIView):
    queryset = RegistroEntrega.objects.all()
    serializer_class = RegistroEntregaSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return RegistroEntregaCreateSerializer
        return RegistroEntregaSerializer

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            logger.info('Registro de entrega criado com sucesso: %s', response.data)
            
            # Produzir mensagem para o Kafka
            for medicamento in response.data['medicamentos']:
                message = {
                    'medicamento': medicamento['codigo_barra'],
                    'posto_distribuicao': response.data['posto_distribuicao']['cnes'],
                    'quantidade': medicamento['quantidade']
                }
                produce_message('estoque_local', message)
                
            return response
        except Exception as e:
            logger.error('Erro ao criar registro de entrega: %s', str(e))
            return Response({'detail': 'Erro ao criar registro de entrega'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def CreateFarmacoBatch(request):
    if not isinstance(request.data, list):
        return Response({"error": "Os dados enviados não são uma lista"}, status=status.HTTP_400_BAD_REQUEST)
    
    if len(request.data) == 0:
        return Response({"error": "A lista de dados está vazia"}, status=status.HTTP_400_BAD_REQUEST)
    
    n_saved = 0
    errors = []

    for entry in request.data:
        try:
            farmaco_serializer = FarmacoSerializer(data=entry)
            if farmaco_serializer.is_valid():
                farmaco_serializer.save()
                n_saved += 1
            else:
                errors.append(farmaco_serializer.errors)
        except Exception as e:
            errors.append(str(e))  # Captura de erros específicos
            
    if errors:
        return Response({"errors": errors}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'nSaved': n_saved}, status=status.HTTP_201_CREATED)