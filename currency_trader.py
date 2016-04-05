from currency_converter import *

class CurrencyTrader:
    def __init__(self, *args):
        self.converter_history = []
        for arg in args:
            if type(arg) == CurrencyConverter:
                self.converter_history.append(arg)
            else:
                raise TypeError

    def get_all_possible_trades(self, this_converter, starting_currency):
        all_possible_trades = []
        for each_currency_code in this_converter.get_available_codes():
            all_possible_trades.append(this_converter.convert(starting_currency, each_currency_code))
        return all_possible_trades

    def convert_all_to_one(self, trades, converter, comparison_currency_code):
        trades_in_one_currency = []
        for each_trade in trades:
            trades_in_one_currency.append(converter.convert(each_trade, comparison_currency_code))
        return trades_in_one_currency

    def get_best_trade(self, possible_trades, trade_history,converter):
        trades_in_one_currency = self.convert_all_to_one(possible_trades, converter, possible_trades[0].currency_code)
        best_value = max(trades_in_one_currency)
        best_index = trades_in_one_currency.index(best_value)
        if len([x for x in trades_in_one_currency if x == best_value]) > 1:
            for x in possible_trades:
                if x == trade_history[-1]:
                    best_index = possible_trades.index(x)
        return possible_trades[best_index]

    def find_trades(self, starting_currency_code):
        starting_value = 100
        possible_trades = [Currency(starting_value, starting_currency_code)]
        trade_history = []
        for each_converter in self.converter_history:
            best_trade = self.get_best_trade(possible_trades, trade_history, each_converter)
            trade_history.append(best_trade)
            possible_trades = self.get_all_possible_trades(each_converter, best_trade)
        trade_history.append([x for x in possible_trades if x.currency_code == starting_currency_code][0])
        return trade_history
