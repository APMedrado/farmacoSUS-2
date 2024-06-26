from django.urls import path
from . import views

# Aqui estão os endpoints

urlpatterns = [
    path('farmacos/', views.FarmacoList.as_view(), name='farmaco-list'),
    path('farmacos/batch/', views.batch_create_farmacos, name='batch-create-farmacos'),
    path('estoque-local/', views.EstoqueLocalList.as_view(), name='estoque-local-list'),
    path('estoque-regional/', views.EstoqueRegionalList.as_view(), name='estoque-regional-list'),
    path('pacientes/', views.PacienteList.as_view(), name='paciente-list'),
    path('medicos/', views.MedicoList.as_view(), name='medico-list'),
    path('registro-entrega/', views.RegistroEntregaList.as_view(), name='registro-entrega-list'),
    path('postos-distribuicao/', views.PostoDistribuicaoList.as_view(), name='posto-distribuicao-list'),
    # path('postos-distribuicao/<str:cnes>/', views.PostoDistribuicaoDetail.as_view(), name='posto-distribuicao-detail')
]
