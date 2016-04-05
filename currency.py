import re
from decimal import *
getcontext().prec =6
class DifferentCurrencyCodeError(TypeError):
    pass

class Currency:
    CURRENCY_SYMBOLS = {'$':'USD', '€':'EUR', '£':'GBP', '¥':'JPY'}
    def __init__(self, *args):
        if len(args) == 2:
            self.value = Decimal(args[0])
            self.currency_code = args[1]
        elif len(args) == 1:
            stripped_input = re.sub(r'[\s,]', '', args[0])
            try:
                self.currency_code = self.CURRENCY_SYMBOLS[stripped_input[0]]
                self.value = Decimal(stripped_input[1:])
            except KeyError:
                raise ValueError("Sorry, currency type {} is not recognized.".format(stripped_input[0]))
            except ValueError as e:
                raise e # Probably bad number format
        else:
            raise TypeError("Expected 3 arguments, recived {}.".format(len(args)+1))

    def __eq__(self, other):
        return(self.currency_code == other.currency_code and self.value == other.value)

    def __gt__(self, other):
        if self.currency_code == other.currency_code:
            return self.value > other.value
        else:
            raise DifferentCurrencyCodeError

    def __lt__(self, other):
        if self.currency_code == other.currency_code:
            return self.value < other.value
        else:
            raise DifferentCurrencyCodeError

    def __add__(self, other):
        if self.currency_code == other.currency_code:
            return Currency(self.value + other.value, self.currency_code)
        else:
            raise DifferentCurrencyCodeError

    def __sub__(self, other):
        if self.currency_code == other.currency_code:
            return Currency(self.value - other.value, self.currency_code)
        else:
            raise DifferentCurrencyCodeError


    def __mul__(self, other):
        if other == Decimal(other):
            return Currency(self.value * Decimal(other), self.currency_code)
        else:
            raise TypeError("Can only multiply by numerics.")

    def __rmul__(self, other):
        if other == Decimal(other):
            return Currency(self.value * Decimal(other), self.currency_code)
        else:
            raise TypeError("Can only multiply by numerics.")

    def __str__(self):
        return(str(self.value) +" "+self.currency_code)
