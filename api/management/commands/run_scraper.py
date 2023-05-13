from django.core.management import BaseCommand
from openpyxl import Workbook, load_workbook
from api.models import CryptoCurrency


class Command(BaseCommand):
    help = 'Cypto Currency'

    # def add_arguments(self, parser):
        # parser.add_argument('number_of_currency')

    def handle(self, *args, **options):

        
        # loading workbook 
        wb = load_workbook(r'C:\Users\CODED\Desktop\cryptude\api\management\commands\cryptoexcel.xlsx')

        ws = wb.active
        
        # ws.append(['Name', 'Symbol', 'Market Cap', 'Price', 'Circulating Supply', 'Volume'])
        
        crypto_currencies = CryptoCurrency.objects.all()
        for crypto in crypto_currencies:
            ws.append([crypto.name, crypto.symbol, crypto.market_cap, crypto.price, crypto.circulating_supply, crypto.volume])
        

        wb.save(r'C:\Users\CODED\Desktop\cryptude\api\management\commands\cryptoexcel.xlsx')

        
        