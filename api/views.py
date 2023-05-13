from django.shortcuts import render
from rest_framework import viewsets, mixins, generics
from api.serializers import CryptoCurrencySerializer
from api.scrape.backgroud_schduler import start
from api.scrape.scrape import ScrapeCryptoCurrency
from api.models import CryptoCurrency
from rest_framework.response import Response
from rest_framework.views import APIView




# Create your views here.

class ScrapeCryptoCurrencyView(APIView):
    
    def post(self, request):
        start()
        
        data = ScrapeCryptoCurrency(request)
        print(data)
        print('data =======')
        CryptoCurrency.objects.create(
            name=data['name'],
            symbol=data['symbol'],
            market_cap=data['market_price'],
            price=data['currency_price'],
            circulating_supply=data['circulating_supply_prince'],
            volume=data['volume']
        )
        return Response({'message':'Currency Created'}, status=201)



class CurrencyRecordViewSet(
    viewsets.GenericViewSet,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin, 
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin
):
    queryset = CryptoCurrency.objects.all()
    serializer_class = CryptoCurrencySerializer


    
        

