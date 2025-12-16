from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Departamento, Projeto, Tecnologia
from .serializers import DepartamentoSerializer, ProjetoSerializer, TecnologiaSerializer

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    # Permissão: Leitura para todos, Escrita apenas para autenticados
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # Filtros: Ativo/Inativo
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['ativo']
    search_fields = ['nome', 'gestor']

class TecnologiaViewSet(viewsets.ModelViewSet):
    queryset = Tecnologia.objects.all()
    serializer_class = TecnologiaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # Filtros: Tipo (Linguagem, Framework, etc)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['tipo']
    search_fields = ['nome']

class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    # Configuração de Filtros poderosos
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    # Filtros exigidos: Departamento, Risco, Tecnologia e Status
    filterset_fields = {
        'departamento': ['exact'],
        'risco': ['exact'],
        'tecnologias': ['exact'],
        'status': ['exact'],
        'data_inicio': ['gte', 'lte', 'exact'],  # gte = maior que, lte = menor que
    }
    
    # Busca textual e Ordenação
    search_fields = ['nome', 'descricao']
    ordering_fields = ['data_inicio', 'nome']