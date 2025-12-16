from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartamentoViewSet, ProjetoViewSet, TecnologiaViewSet

# O Router cria as rotas automaticamente (GET, POST, PUT, DELETE)
router = DefaultRouter()
router.register('departamentos', DepartamentoViewSet)
router.register('projetos', ProjetoViewSet)
router.register('tecnologias', TecnologiaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]