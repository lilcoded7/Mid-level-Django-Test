from rest_framework import serializers 
from api.models import CryptoCurrency


class CryptoCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model  = CryptoCurrency
        fields = '__all__'