import re
from decimal import *
getcontext().prec =6
class DifferentCurrencyCodeError(TypeError):
    pass

class Currency:
    CURRENCY_SYMBOLS = {'$':'USD', '€':'EUR','£':'GBP','¥':'JPY'}
    def __init__(self,*args):
        if len(args) == 2:
            self.value = Decimal(args[0])
            self.currency_code = args[1]
        elif len(args) == 1:
            raise NotImplementedError('Not there yet')
            self.currency_code(CURRENCY_SYMBOLS[args])
        else:
            raise TypeError("Expected 3 arguments, recived {}.".format(len(args)+1))

    def __eq__(self,other):
        return(self.currency_code == other.currency_code and self.value == other.value)

    def __add__(self,other):
        if self.currency_code == other.currency_code:
            return Currency(self.value + other.value,self.currency_code)
        else:
            raise DifferentCurrencyCodeError

    def __sub__(self,other):
        if self.currency_code == other.currency_code:
            return Currency(self.value - other.value,self.currency_code)
        else:
            raise DifferentCurrencyCodeError


    def __mul__(self,other):
        if other == Decimal(other):
            return Currency(self.value * Decimal(other),self.currency_code)
        else:
            raise TypeError("Can only multiply by numerics.")

    def __rmul__(self,other):
        if other == Decimal(other):
            return Currency(self.value * Decimal(other),self.currency_code)
        else:
            raise TypeError("Can only multiply by numerics.")

    def __str__(self):
        return(str(self.value) +" "+self.currency_code)
