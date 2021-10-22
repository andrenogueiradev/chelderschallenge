from django.contrib.auth.models import User
from rest_framework import serializers
from accounts.models import Client, User    


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['first_name','last_name', 'cpf', 'document', 'email', 'password', 'is_active', 'is_admin']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'cpf', 'email', 'document']


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name']
        extra_kwargs = {'password': {'write_only' : True}}
