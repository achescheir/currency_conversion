import unittest
from currency_trader import CurrencyTrader
from currency_converter import CurrencyConverter
from currency import Currency

class TestCurrencyTrader(unittest.TestCase):
    def test_2_argument_constructor(self):
        converter1 = CurrencyConverter({'USD':1.0,'GBP':0.5})
        converter2 = CurrencyConverter({'USD':1.0,'GBP':0.25})
        self.assertEqual(CurrencyTrader(converter1,converter2).converter_history,[converter1,converter2])


    def test_1_round_trade(self):
        converter1 = CurrencyConverter({'USD':1.0,'GBP':0.5})
        converter2 = CurrencyConverter({'USD':1.0,'GBP':0.25})
        trader = CurrencyTrader(converter1,converter2)
        self.assertEqual(trader.find_trades('USD'),[Currency(100,'USD'),Currency(50,'GBP'),Currency(200,'USD')])

    def test_1_round_hold(self):
        pass

    def test_1_round_either(self):
        pass

    def test_multiargument_constructor(self):
        pass

    def test_3_round_trade(self):
        pass

    def test_3_round_with_hold(self):
        pass

    def test_3_round_with_either(self):
        pass

if __name__ == '__main__':
    unittest.main()
