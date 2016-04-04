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
        converter1 = CurrencyConverter({'USD':1.0,'GBP':0.5})
        converter2 = CurrencyConverter({'USD':1.0,'GBP':1.0})
        trader = CurrencyTrader(converter1,converter2)
        self.assertEqual(trader.find_trades('USD'),[Currency(100,'USD'),Currency(100,'USD'),Currency(100,'USD')])


    def test_1_round_either(self):
        converter1 = CurrencyConverter({'USD':1.0,'GBP':0.5})
        converter2 = CurrencyConverter({'USD':1.0,'GBP':0.5})
        trader = CurrencyTrader(converter1,converter2)
        self.assertEqual(trader.find_trades('USD'),[Currency(100,'USD'),Currency(100,'USD'),Currency(100,'USD')])


    def test_multiargument_constructor(self):
        converter1 = CurrencyConverter({'USD':1.0,'GBP':0.5})
        converter2 = CurrencyConverter({'USD':1.0,'GBP':0.25,'JPY':100})
        converter3 = CurrencyConverter({'USD':1.0,'GBP':0.25,'JPY':50})
        self.assertEqual(CurrencyTrader(converter1,converter2,converter3).converter_history,[converter1,converter2,converter3])


    def test_3_round_trade(self):
        converter1 = CurrencyConverter({'USD':1.0,'GBP':0.5})
        converter2 = CurrencyConverter({'USD':1.0,'GBP':0.25,'JPY':100})
        converter3 = CurrencyConverter({'USD':1.0,'GBP':0.25,'JPY':50})
        trader = CurrencyTrader(converter1,converter2,converter3)
        self.assertEqual(trader.find_trades('USD'),[Currency(100,'USD'),Currency(50,'GBP'),Currency(20000,'JPY'),Currency(400,'USD')])

    def test_3_round_with_hold(self):
        converter1 = CurrencyConverter({'USD':1.0,'GBP':0.5})
        converter2 = CurrencyConverter({'USD':1.0,'GBP':0.25,'JPY':50})
        converter3 = CurrencyConverter({'USD':1.0,'GBP':0.2,'JPY':50})
        trader = CurrencyTrader(converter1,converter2,converter3)
        self.assertEqual(trader.find_trades('USD'),[Currency(100,'USD'),Currency(50,'GBP'),Currency(50,'GBP'),Currency(250,'USD')])


    def test_3_round_with_either(self):
        converter1 = CurrencyConverter({'USD':1.0,'GBP':0.5})
        converter2 = CurrencyConverter({'USD':1.0,'GBP':0.25,'JPY':50})
        converter3 = CurrencyConverter({'USD':1.0,'GBP':0.25,'JPY':50})
        trader = CurrencyTrader(converter1,converter2,converter3)
        self.assertEqual(trader.find_trades('USD'),[Currency(100,'USD'),Currency(50,'GBP'),Currency(50,'GBP'),Currency(200,'USD')])


if __name__ == '__main__':
    unittest.main()
