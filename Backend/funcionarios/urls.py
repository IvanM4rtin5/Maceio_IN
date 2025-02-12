from django.urls import path
from .views import register_user
from django.urls import path, include
from .views import FuncionarioViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'funcionarios', FuncionarioViewSet)

urlpatterns = [
    path('api/register/', register_user, name='register'),
    path('api/', include(router.urls)),
]