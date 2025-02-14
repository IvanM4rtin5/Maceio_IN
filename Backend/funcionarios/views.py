from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models.funcionario import Funcionario
from .models.user import CustomUser  
from .serializers import FuncionarioSerializer, UserSerializer
from django.views.decorators.csrf import csrf_exempt

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    permission_classes = [IsAuthenticated]

@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                "message": "User registered successfully.",
                "token": token.key
            }, status=201)
        return Response(serializer.errors, status=400)

@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def login_with_email(request):
    email = request.data.get("email")
    password = request.data.get("password")

    if not email or not password:
        return Response({
            "error": "Email e senha são obrigatórios"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Verifica se o usuário existe
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({
                "error": "Usuário não encontrado"
            }, status=status.HTTP_404_NOT_FOUND)

        # Tenta autenticar o usuário
        user = authenticate(request, username=email, password=password)
        
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key,
                "user": {
                    "id": user.id,
                    "email": user.email,
                    # "name": user.get_full_name() if user.get_full_name() else user.email
                }
            })
        else:
            return Response({
                "error": "Senha inválida"
            }, status=status.HTTP_401_UNAUTHORIZED)
            
    except Exception as e:
        return Response({
            "error": "Erro ao realizar login",
            "detail": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)