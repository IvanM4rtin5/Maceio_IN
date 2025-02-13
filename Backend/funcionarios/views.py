from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models.funcionario import Funcionario
from .models.user import CustomUser
from .serializers import FuncionarioSerializer, UserSerializer

# ViewSet para Funcionarios
class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    permission_classes = [IsAuthenticated]

# View para registro de usuários
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({"message": "User registered successfully."}, status=201)
    return Response(serializer.errors, status=400)

# View para login usando email e senha
@api_view(['POST'])
@permission_classes([AllowAny])
def login_with_email(request):
    email = request.data.get("email")
    password = request.data.get("password")

    if not email or not password:
        return Response({"error": "Email e senha são obrigatórios"}, status=status.HTTP_400_BAD_REQUEST)

    # O 'authenticate' agora usará o EmailBackend
    user = authenticate(username=email, password=password)

    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})
    else:
        return Response({"error": "Email ou senha inválidos"}, status=status.HTTP_401_UNAUTHORIZED)
