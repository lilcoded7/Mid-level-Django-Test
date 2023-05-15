from django.shortcuts import render
from rest_framework import viewsets, mixins, generics
from api.serializers import CryptoCurrencySerializer
from api.models import CryptoCurrency
from rest_framework.response import Response
from rest_framework.views import APIView
from api.background_task import ScrapeCryptoCurrency
from api.utils import updata_objects_if_exist, create_new_objects


# Create your views here.

class ScrapeCryptoCurrencyView(APIView):

    def post(self, request):
        # Check if there are any existing CryptoCurrency objects in the database
        crypto_currencies = CryptoCurrency.objects.all()
        if crypto_currencies.exists():
            # If there are existing objects, update them
            ScrapeCryptoCurrency.delay()
            updata_objects_if_exist()        
        else:
            # If there are no existing objects, create new objects
            create_new_objects()
        return Response({'message':'scraper is running'}, status=201)




class CurrencyRecordViewSet(
    viewsets.GenericViewSet,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin, 
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin
):
    queryset = CryptoCurrency.objects.all()
    serializer_class = CryptoCurrencySerializer


    
        

