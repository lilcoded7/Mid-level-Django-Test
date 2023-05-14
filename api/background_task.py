from bs4 import BeautifulSoup
from api.models import CryptoCurrency
import requests 
from celery import shared_task


@shared_task(bind=True)
def ScrapeCryptoCurrency(self):
    cryptocurrency = {
        'names':[],
        'symbols':[],
        'market_cap':[],
        'prices':[],
        'circulating_supply':[],
        'volumes':[]
    }

    url = 'https://coinmarketcap.com/all/views/all/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # scrape crypto names 
    currency_name = soup.find_all(class_='cmc-table__column-name--name cmc-link')
    for names in currency_name:
        name = names.text
        cryptocurrency['names'].append(name)
    
        
    # scrape currency symbol from coinmarketcap     
    currency_symbol = soup.find_all(class_='cmc-table__column-name--symbol cmc-link')
    for symbols in currency_symbol:
        symbol = symbols.text
        cryptocurrency['symbols'].append(symbol)
        

    # scrape crypto market cap prices
    market_cap = soup.find_all(class_='sc-edc9a476-1 gqomIJ')
    for cap_prices in market_cap:
        market_cap_price = cap_prices.text
        
        cryptocurrency['market_cap'].append(market_cap_price)
        

    # get current crypto prices 
    currency_prices = soup.find_all(class_='sc-cadad039-0 clgqXO')
    for price in currency_prices:
        currency_price = price.text
        # break
        cryptocurrency['prices'].append(currency_price)
    
    # get circulating_supply form coinmarketcap
    circulating_supply = soup.find_all(class_='cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__circulating-supply')
    for circulating_sup in circulating_supply:
        circulating_supply_prince = circulating_sup.text
        # break
        cryptocurrency['circulating_supply'].append(circulating_supply_prince)

    currency_volume = soup.find_all(class_='cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__volume-24-h')
    for volumes in currency_volume:
        volume = volumes.text
        # break
        cryptocurrency['volumes'].append(volume)
    
    return cryptocurrency



