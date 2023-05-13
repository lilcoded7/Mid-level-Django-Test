from django.db import models
from cryptude.basemodel import TimeBaseModel



class CryptoCurrency(TimeBaseModel):
    name       = models.CharField(max_length=100)
    symbol     = models.CharField(max_length=100)
    market_cap = models.CharField(max_length=100)
    price      = models.CharField(max_length=100)
    circulating_supply = models.CharField(max_length=100)
    volume     = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name 
