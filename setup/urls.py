from django.contrib import admin
from django.urls import path, include

# Importações para a documentação (Swagger)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuração da aparência da Documentação
schema_view = get_schema_view(
    openapi.Info(
        title="API InnovaBank",
        default_version='v1',
        description="API para gestão de portfólio de TI do InnovaBank",
        contact=openapi.Contact(email="pmo@innovabank.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# --- PERSONALIZAÇÃO DO ADMIN (NOVO) ---
admin.site.site_header = "Administração InnovaBank"
admin.site.site_title = "Portal PMO"
admin.site.index_title = "Gestão de Portfólio de TI"

urlpatterns = [
    path('admin/', admin.site.urls),

    # Aqui conectamos as rotas do seu app 'gestao'
    path('api/', include('gestao.urls')),

    # Rota para acessar a documentação Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]