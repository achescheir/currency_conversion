from currency import Currency

class CurrencyConverter():
    def __init__(self,conversion_rates):
        self.conversion_rates = conversion_rates

    def convert(self,source_currency, target_code):
        conversion_rate = self.conversion_rates[source_currency.currency_code] / self.conversion_rates[target_code]
        return(Currency(source_currency.value * conversion_rate,target_code))
