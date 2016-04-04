from currency_converter import *

class CurrencyTrader:
    def __init__(self,*args):
        self.converter_history = []
        for arg in args:
            if type(arg) == CurrencyConverter:
                converter_history.append(arg)
            else:
                raise TypeError

    def find_trades(self):
        pass
    
