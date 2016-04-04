from currency_converter import *

class CurrencyTrader:
    def __init__(self,*args):
        self.converter_history = []
        for arg in args:
            if type(arg) == CurrencyConverter:
                self.converter_history.append(arg)
            else:
                raise TypeError

    def get_all_trades(self, this_converter, starting_currency):
        all_possible_trades = []
        for each_currency_code in this_converter.get_available_codes():
            all_possible_trades.append(this_converter.convert(starting_currency,each_currency_code))
        return all_possible_trades

    def find_trades(self,starting_currency_code):
        starting_value = 100
        possible_trades = [Currency(starting_value,starting_currency_code)]
        trade_history = []
        for each_converter in self.converter_history:
            possible_trades_in_starting_currency = []
            for each_possible_trade in possible_trades:
                possible_trades_in_starting_currency.append(each_converter.convert(each_possible_trade,starting_currency_code))
            best_value = max(possible_trades_in_starting_currency)
            best_index = possible_trades_in_starting_currency.index(best_value)
            if len([x for x in possible_trades_in_starting_currency if x == best_value]) > 1:
                for x in possible_trades:
                    if x == trade_history[-1]:
                        best_index = possible_trades.index(x)
            best_trade = possible_trades[best_index]
            trade_history.append(best_trade)
            possible_trades = self.get_all_trades(each_converter,best_trade)
        trade_history.append([x for x in possible_trades if x.currency_code == starting_currency_code][0])
        return trade_history
