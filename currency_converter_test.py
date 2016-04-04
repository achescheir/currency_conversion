import unittest
from currency_converter import CurrencyConverter
from currency import Currency
from decimal import *
getcontext().prec = 6
class TestCurrencyConverter(unittest.TestCase):
    def test_2_code_constructor(self):
        self.assertEqual(CurrencyConverter({'USD':1.0,'GBP':0.70}).conversion_rates, {'USD':1.0,'GBP':0.70})

    def test_multicode_constructor(self):
        self.assertEqual(CurrencyConverter({'USD':1.0,'GBP':0.70,'JPY':111.3}).conversion_rates, {'USD':1.0,'GBP':0.70,'JPY':111.3})


    def test_conversion_to_own_code(self):
        test_converter = CurrencyConverter({'USD':1.0,'GBP':0.70})
        test_currency = Currency(5,'USD')
        self.assertEqual(test_converter.convert(test_currency,'USD'),test_currency)

    def test_conversion_to_2nd_code(self):
        test_converter = CurrencyConverter({'USD':1.0,'GBP':0.70})
        test_currency = Currency(5,'USD')
        equal_currency = Currency(Decimal(5)*Decimal(0.70),'GBP')
        self.assertEqual(test_converter.convert(test_currency,'GBP'),equal_currency)

    def test_conversion_to_3rd_code(self):
        test_converter = CurrencyConverter({'USD':1.0,'GBP':0.70,'JPY':111.3})
        test_currency = Currency(5,'GBP')
        equal_currency = Currency(Decimal(5) * Decimal(111.3) / Decimal(0.70),'JPY')
        self.assertEqual(test_converter.convert(test_currency,'JPY'),equal_currency)

    def test_get_available_codes(self):
        test_converter = CurrencyConverter({'USD':1.0,'GBP':0.70,'JPY':111.3})
        self.assertEqual(sorted(test_converter.get_available_codes()),['GBP','JPY','USD'])

    def test_conversion_to_unknown_code(self):
        pass

    def test_conversion_from_unknown_code(self):
        pass


if __name__ == '__main__':
    unittest.main()
