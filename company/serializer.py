from rest_framework import serializers
from company.models import Company    


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['company_name', 'cnpj', 'address', 'city', 'status']