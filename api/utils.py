from scrape.scrape_data import ScrapeCryptoCurrency


def get_currency_value():

    currency = ScrapeCryptoCurrency()
    names = currency.get_currency_name()

    for name in names:
        print(name)

    

get_currency_value()