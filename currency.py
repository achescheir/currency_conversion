import re

class Currency:
    CURRENCY_SYMBOLS = {'$':'USD', '€':'EUR','£':'GBP','¥':'JPY'}
    def __init__(self,*args):
        if len(args) == 2:
            self.value = float(args[0])
            self.currency_code = args[1]
        elif len(args) == 1:
            raise NotImplementedError('Not there yet')
            self.currency_code(CURRENCY_SYMBOLS[args])
        else:
            raise TypeError("Expected 3 arguments, recived {}.".format(len(args)+1))

    def __eq__(self,other):
        return(self.currency_code == other.currency_code and self.value == other.value)

    def __add__(self,other):
        pass

    def __sub__(self,other):
        pass

    def __mul__(self,other):
        pass
