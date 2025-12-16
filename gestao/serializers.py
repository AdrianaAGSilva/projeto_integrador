from rest_framework import serializers
from .models import Departamento, Projeto, Tecnologia

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

class TecnologiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnologia
        fields = '__all__'

class ProjetoSerializer(serializers.ModelSerializer):
    # Para exibir o nome do departamento e tecnologias em vez de apenas o ID
    departamento_nome = serializers.ReadOnlyField(source='departamento.nome')
    tecnologias_nomes = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Projeto
        fields = '__all__'