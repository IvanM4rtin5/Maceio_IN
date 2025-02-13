from django.urls import path, include
from .views import FuncionarioViewSet, register_user, login_with_email
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'funcionarios', FuncionarioViewSet, basename='funcionario')

urlpatterns = [
    path('api/register/', register_user, name='register'),  # Registro de usuários
    path('api/login/', login_with_email, name='login_with_email'),  # Login com email e senha
    path('api/', include(router.urls)),  # Rotas do viewset
]
