from django.contrib import admin
from .models import Departamento, Tecnologia, Projeto

# Isso faz as tabelas aparecerem na tela azul
admin.site.register(Departamento)
admin.site.register(Tecnologia)
admin.site.register(Projeto)