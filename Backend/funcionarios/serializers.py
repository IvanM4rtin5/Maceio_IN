from rest_framework import serializers
from .models.funcionario import Funcionario
from .models.user import CustomUser
from django.contrib.auth.models import User

# serializer para Funcionario
class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['id', 'nome', 'email', 'setor', 'created_at', 'updated_at']

# serializer para User (registro)
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ( 'email', 'nome', 'password')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            nome=validated_data['nome'],
            password=validated_data['password']
        )
        return user