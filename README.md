# currency_conversion

## Currency

Currency objects represent an amount of a particular currency. They can be added
or subtracted together if they have the same currency and multiplied by regular
numbers. They can be created either by specifying the currency and amount
separately, or by adding a currency symbol onto the beginning of the amount.
Currency objects can be converted from one currency to another using a
CurrencyConverter object.

## CurrencyConverter

CurrencyConverter objects store the relationship between several different
currencies. They can be used to convert from one currency to another. They are
created by passing in a dict with the keys representing the currency codes and
the values representing an amount of each currency that has equal value.

## CurrencyTrader

CurrencyTrader objects contain a history of several CurrencyConverters that
were available at different points in time in order. The find_trades() method
allows the user to retrospectively determine which course of trades would have
given the greatest return starting and ending in the same currency. The trades
are listed from the initial state to the final state in terms of the percentage
of the starting amount of the starting currency that the user would have after
each trade
