from rest_framework_mongoengine import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Farmaco, EstoqueLocal, EstoqueRegional, Paciente, Medico, RegistroEntrega, PostoDistribuicao
from .serializers import FarmacoSerializer, EstoqueLocalSerializer, EstoqueRegionalSerializer, PacienteSerializer, MedicoSerializer, RegistroEntregaSerializer, PostoDistribuicaoSerializer
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

class EstoqueLocalList(generics.ListCreateAPIView):
    queryset = EstoqueLocal.objects.all()
    serializer_class = EstoqueLocalSerializer

class EstoqueRegionalList(generics.ListCreateAPIView):
    queryset = EstoqueRegional.objects.all()
    serializer_class = EstoqueRegionalSerializer

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

@api_view(['POST'])
def batch_create_farmacos(request):
    if isinstance(request.data, list):
        serializer = FarmacoSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({"detail": "Invalid data format. Expected a list."}, status=status.HTTP_400_BAD_REQUEST)
