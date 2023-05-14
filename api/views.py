from django.shortcuts import render
from rest_framework import viewsets, mixins, generics
from api.serializers import CryptoCurrencySerializer
from api.models import CryptoCurrency
from rest_framework.response import Response
from rest_framework.views import APIView
from api.background_task import ScrapeCryptoCurrency



# Create your views here.


class ScrapeCryptoCurrencyView(APIView):

    def post(self, request):
        # Check if there are any existing CryptoCurrency objects in the database
        crypto_currencies = CryptoCurrency.objects.all()
        print(crypto_currencies)
        print('====================')
        if crypto_currencies.exists():
            # If there are existing objects, update them
            ScrapeCryptoCurrency.delay()
            cryptocurrency_data = ScrapeCryptoCurrency()
            for i in range(len(cryptocurrency_data['names'])):
                name = cryptocurrency_data['names'][i]
                symbol = cryptocurrency_data['symbols'][i]
                market_cap = cryptocurrency_data['market_cap'][i]
                price = cryptocurrency_data['prices'][i]
                circulating_supply = cryptocurrency_data['circulating_supply'][i]
                volume = cryptocurrency_data['volumes'][i]

                # Update existing objects
                try:
                    crypto_currency = CryptoCurrency.objects.get(name=name)
                    crypto_currency.symbol = symbol
                    crypto_currency.market_cap = market_cap
                    crypto_currency.price = price
                    crypto_currency.circulating_supply = circulating_supply
                    crypto_currency.volume = volume
                    crypto_currency.save()
                # If object does not exist, create new object
                except CryptoCurrency.DoesNotExist:
                    CryptoCurrency.objects.create(
                        name=name,
                        symbol=symbol,
                        market_cap=market_cap,
                        price=price,
                        circulating_supply=circulating_supply,
                        volume=volume
                    )
        else:
            # If there are no existing objects, create new objects
            ScrapeCryptoCurrency.delay()
            cryptocurrency_data = ScrapeCryptoCurrency()
            for i in range(len(cryptocurrency_data['names'])):
                name = cryptocurrency_data['names'][i]
                symbol = cryptocurrency_data['symbols'][i]
                market_cap = cryptocurrency_data['market_cap'][i]
                price = cryptocurrency_data['prices'][i]
                circulating_supply = cryptocurrency_data['circulating_supply'][i]
                volume = cryptocurrency_data['volumes'][i]

                CryptoCurrency.objects.create(
                    name=name,
                    symbol=symbol,
                    market_cap=market_cap,
                    price=price,
                    circulating_supply=circulating_supply,
                    volume=volume
                )

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


    
        

