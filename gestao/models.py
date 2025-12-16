from django.db import models

class Departamento(models.Model):
    # [cite_start]Requisitos do PDF: id (automático), nome, gestor, descrição, ativo, data de criação [cite: 27]
    nome = models.CharField(max_length=100)
    gestor = models.CharField(max_length=100)
    descricao = models.TextField(verbose_name="Descrição")
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Tecnologia(models.Model):
    # [cite_start]Requisitos do PDF: id, nome, tipo, versão, fornecedor, descrição [cite: 30]
    TIPO_CHOICES = [
        ('linguagem', 'Linguagem'),
        ('framework', 'Framework'),
        ('cloud', 'Serviço Cloud'),
        ('banco', 'Banco de Dados'),
        ('outros', 'Outros'),
    ]
    
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    versao = models.CharField(max_length=50, blank=True, null=True)
    fornecedor = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField(verbose_name="Descrição", blank=True)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    # [cite_start]Requisitos do PDF: id, nome, descrição, datas, status [cite: 28]
    STATUS_CHOICES = [
        ('planejado', 'Planejado'),
        ('em_execucao', 'Em Execução'),
        ('concluido', 'Concluído'),
        ('cancelado', 'Cancelado'),
    ]
    
    # [cite_start]Adicionado para atender o filtro de risco exigido na página 2 [cite: 48]
    RISCO_CHOICES = [ 
        ('baixo', 'Baixo'),
        ('medio', 'Médio'),
        ('alto', 'Alto'),
    ]

    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planejado')
    
    # [cite_start]Campo extra necessário para atender o requisito de "Alterar orçamento" [cite: 43]
    orcamento = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    
    risco = models.CharField(max_length=10, choices=RISCO_CHOICES, default='baixo')

    # Relacionamentos
    # [cite_start]Um projeto tem um departamento [cite: 31]
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name='projetos')
    # [cite_start]Um projeto tem várias tecnologias [cite: 32]
    tecnologias = models.ManyToManyField(Tecnologia, related_name='projetos')

    def __str__(self):
        return self.nome
