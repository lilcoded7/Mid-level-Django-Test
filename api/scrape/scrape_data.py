# from api.models import CryptoCurrency
from bs4 import BeautifulSoup
import requests 



class ScrapeCryptoCurrency:
    

    def __init__(self):
        url = 'https://coinmarketcap.com/all/views/all/'
        response = requests.get(url)
        self.soup = BeautifulSoup(response.text, 'html.parser')

    def get_currency_name(self):
       
        currency_name = self.soup.find_all(class_='cmc-table__column-name--name cmc-link')
        for names in currency_name:
            name = names.text
            
        

    def get_currency_symbol(self):
        currency_symbol = self.soup.find_all(class_='cmc-table__column-name--symbol cmc-link')
        for symbols in currency_symbol:
            symbol = symbols.text
            return symbol

    def get_market_cap(self):
        market_cap = self.soup.find(class_='sc-edc9a476-1 gqomIJ')
        for cap_prices in market_cap:
            market_price = cap_prices.text
            return market_price

    def get_currency_prices(self):
        currency_prices = self.soup.find(class_='sc-cadad039-0 clgqXO').text
        
            

    def get_circulating_supply(self):
        circulating_sup = self.soup.find(class_='cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__circulating-supply').text
        

    def get_volume(self):
        currency_volume = self.soup.find_all(class_='cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__volume-24-h')
        for volumes in currency_volume:
            volume = volumes.text
            return volume

    # def save_scrape_data_to_database(self):
    #     CryptoCurrency.objects.create(name=self.name, symbol=self.symbol, market_cap=self.cap_price, price=self.price, circulating_supply=self.value, volume=self.volume)

            
        

cryptude = ScrapeCryptoCurrency()
cryptude.get_currency_name()
# print('===============Next============')
# cryptude.get_currency_symbol()
# print('===============Next============')
# cryptude.get_market_cap()
# print('===============Next============')
# cryptude.get_currency_prices()
# print('===============Next============')
# cryptude.get_circulating_supply()
# print('===============Next============')
# cryptude.get_volume()
# print('===============All Pass============')