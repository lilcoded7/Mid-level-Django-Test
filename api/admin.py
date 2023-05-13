from django.contrib import admin
from .models import CryptoCurrency

# Register your models here.



# Modify admin page 
admin.site.site_header= 'Crypto Currency'
admin.site.site_title = 'Crypto Currency'

# Model List
class CryptoCurrencyAdmin(admin.ModelAdmin):
    list_display = ['name', 'symbol', 'market_cap', 'price', 'circulating_supply', 'volume']


admin.site.register(CryptoCurrency, CryptoCurrencyAdmin)