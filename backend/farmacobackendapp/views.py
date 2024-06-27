from rest_framework_mongoengine import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Farmaco, EstoqueLocal, EstoqueRegional, Paciente, Medico, RegistroEntrega, PostoDistribuicao
from .serializers import FarmacoSerializer, EstoqueLocalSerializer, EstoqueLocalCreateSerializer, EstoqueRegionalSerializer, PacienteSerializer, MedicoSerializer, RegistroEntregaSerializer, PostoDistribuicaoSerializer
import logging

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
    
    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            logger.info('Medicamento adicionado ao estoque regional com sucesso: %s', response.data)
            return response
        except Exception as e:
            logger.error('Erro ao adicionar medicamento ao estoque regional: %s', str(e))
            return Response({'detail': 'Erro ao adicionar medicamento ao estoque regional'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PacienteList(generics.ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class MedicoList(generics.ListCreateAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class RegistroEntregaList(generics.ListCreateAPIView):
    queryset = RegistroEntrega.objects.all()
    serializer_class = RegistroEntregaSerializer

class PostoDistribuicaoList(generics.ListCreateAPIView):
    queryset = PostoDistribuicao.objects.all()
    serializer_class = PostoDistribuicaoSerializer

class PostoDistribuicaoDetail(generics.RetrieveAPIView):
    queryset = PostoDistribuicao.objects.all()
    serializer_class = PostoDistribuicaoSerializer
    lookup_field = 'cnes'

@api_view(['POST'])
def batch_create_farmacos(request):
    if isinstance(request.data, list):
        tam = len(request.data)
        for entry in request.data:
            try:
                farmaco = Farmaco(entry)
                farmaco.save()
            except Exception :
                return Response({"Um item não é um farmaco"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'nSaved': tam}, status=status.HTTP_201_CREATED)        
                
