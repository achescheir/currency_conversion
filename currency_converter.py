from currency import Currency
from decimal import *
getcontext().prec = 6

class UnkownCurrencyError(ValueError):
    pass

class CurrencyConverter():
    def __init__(self, conversion_rates):
        self.conversion_rates = {}
        for key in conversion_rates:
            self.conversion_rates[key] = Decimal(conversion_rates[key])

    def convert(self, source_currency, target_code):
        if target_code not in self.conversion_rates or source_currency.currency_code not in self.conversion_rates:
            raise UnkownCurrencyError()
        conversion_rate = self.conversion_rates[target_code] / self.conversion_rates[source_currency.currency_code]
        return(Currency(source_currency.value * conversion_rate, target_code))

    def get_available_codes(self):
        return self.conversion_rates.keys()
