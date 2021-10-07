from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from accounts.models import Client, Company, User    


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['first_name', 'cpf', 'email', 'document']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['company_name', 'cnpj', 'address', 'city', 'status', 'email']  


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
