from django.urls import path
from . import views

# Aqui estão os endpoints

urlpatterns = [
    path('estoque-local/', views.EstoqueLocalList.as_view(), name='estoque-local-list'),
    path('estoque-local/batch/', views.CreateEstoqueLocalBatch, name='create-estoque-local-batch'),
    path('estoque-regional/', views.EstoqueRegionalList.as_view(), name='estoque-regional-list'),
    path('estoque-regional/batch/', views.CreateEstoqueRegionalBatch, name='create-estoque-regional-batch'),
    path('farmacos/', views.FarmacoList.as_view(), name='farmaco-list'),
    path('farmacos/batch/', views.CreateFarmacoBatch, name='create-farmaco-batch'),
    path('farmacos/<str:codigo_barra>/', views.FarmacoDetail.as_view(), name='farmaco-detail'),
    path('medicos/', views.MedicoList.as_view(), name='medico-list'),
    path('medicos/<str:crm>/', views.MedicoDetail.as_view(), name='medico-detail'),
    path('pacientes/', views.PacienteList.as_view(), name='paciente-list'),
    path('pacientes/<str:cpf>/', views.PacienteDetail.as_view(), name='paciente-detail'),
    path('postos-distribuicao/', views.PostoDistribuicaoList.as_view(), name='posto-distribuicao-list'),
    path('postos-distribuicao/<str:cnes>/', views.PostoDistribuicaoDetail.as_view(), name='posto-distribuicao-detail'),
    path('registros-entregas/', views.RegistroEntregaListCreateView.as_view(), name='registro-entrega-list-create'),
]
