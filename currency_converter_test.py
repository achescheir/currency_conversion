import unittest
from currency_converter import CurrencyConverter
from currency import Currency

class TestCurrencyConverter(unittest.TestCase):
    def test_2_code_constructor(self):
        self.assertEqual(CurrencyConverter({'USD':1.0,'GBP':1.43}).conversion_rates, {'USD':1.0,'GBP':1.43})

    def test_multicode_constructor(self):
        pass

    def test_conversion_to_own_code(self):
        test_converter = CurrencyConverter({'USD':1.0,'GBP':1.43})
        test_currency = Currency(5,'USD')
        self.assertEqual(test_converter.convert(test_currency,'USD'),test_currency)

    def test_conversion_to_2nd_code(self):
        test_converter = CurrencyConverter({'USD':1.0,'GBP':1.43})
        test_currency = Currency(5,'USD')
        equal_currency = Currency(5/1.43,'GBP')
        self.assertEqual(test_converter.convert(test_currency,'GBP'),equal_currency)

    def test_conversion_to_3rd_code(self):
        pass

    def test_conversion_to_unknown_code(self):
        pass

    def test_conversion_from_unknown_code(self):
        pass


if __name__ == '__main__':
    unittest.main()
