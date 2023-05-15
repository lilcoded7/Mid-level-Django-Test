from api.background_task import ScrapeCryptoCurrency
from api.models import CryptoCurrency


def updata_objects_if_exist():
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



def create_new_objects():
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







