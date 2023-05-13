from bs4 import BeautifulSoup
from api.models import CryptoCurrency
import requests 

def ScrapeCryptoCurrency(request):
    
    url = 'https://coinmarketcap.com/all/views/all/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    currency_name = soup.find_all(class_='cmc-table__column-name--name cmc-link')
    for names in currency_name:
        name = names.text
        
        print('-=--=-=-==-=-=-=-=-==-=-=-=-=-=-=-=-=-=')
    # get currency symbol from coinmarketcap     
    currency_symbol = soup.find_all(class_='cmc-table__column-name--symbol cmc-link')
    for symbols in currency_symbol:
        symbol = symbols.text
        
        # print(symbol)
    print('-=--=-=-==-=-=-=-=-==-=-=-=-=-=-=-=-=-=')

    market_cap = soup.find(class_='sc-edc9a476-1 gqomIJ')
    for cap_prices in market_cap:
        market_price = cap_prices.text
        
        # print(market_price)
    print('-=--=-=-==-=-=-=-=-==-=-=-=-=-=-=-=-=-=')
    
    # get current crypto prices 
    currency_prices = soup.find_all(class_='sc-cadad039-0 clgqXO')
    for price in currency_prices:
        currency_price = price.text
        
        # print(currency_price)
    print('-=--=-=-==-=-=-=-=-==-=-=-=-=-=-=-=-=-=')
    
    # get circulating_supply form coinmarketcap
    circulating_supply = soup.find_all(class_='cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__circulating-supply')
    for circulating_sup in circulating_supply:
        circulating_supply_prince = circulating_sup.text
       
        # print(circulating_supply_prince)
    print('-=--=-=-==-=-=-=-=-==-=-=-=-=-=-=-=-=-=')
        
    
    currency_volume = soup.find_all(class_='cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__volume-24-h')
    for volumes in currency_volume:
        volume = volumes.text
    
        print(volume)
        print('OKAY')
    # print(currencies)
    
        
    return {'name':name, 'symbol':symbol,'market_price':market_price, 'currency_price':currency_price, 'circulating_supply_prince':circulating_supply_prince, 'volume':volume}



