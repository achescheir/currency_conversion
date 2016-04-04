import unittest
from currency import *

class TestCurrency(unittest.TestCase):

    def test_1_arg_init(self):
        pass

    def test_2_arg_init(self):
        test_currency = Currency(5, 'USD')
        self.assertTrue(test_currency.currency_code is 'USD')
        self.assertTrue(test_currency.value == 5.00)

    def test_equality(self):
        test_currency1 = Currency(5, 'USD')
        test_currency2 = Currency(5, 'USD')
        self.assertEqual(test_currency1 , test_currency2)

    def test_equality_different_value(self):
        test_currency1 = Currency(5, 'USD')
        test_currency2 = Currency(10, 'USD')
        self.assertNotEqual(test_currency1 , test_currency2)

    def test_equality_different_code(self):
        test_currency1 = Currency(5, 'USD')
        test_currency2 = Currency(5, 'GBP')
        self.assertNotEqual(test_currency1 , test_currency2)

    def test_comparisons(self):
        pass

    def test_addition_same_code(self):
        test_currency1 = Currency(5, 'USD')
        test_currency2 = Currency(10, 'USD')
        self.assertEqual(test_currency1 + test_currency2, Currency(15.00,'USD'))

    def test_addition_different_code(self):
        test_currency1 = Currency(5, 'USD')
        test_currency2 = Currency(5, 'GBP')
        with self.assertRaises(DifferentCurrencyCodeError):
            test_currency1 + test_currency2


    def test_subtraction_same_code(self):
        test_currency1 = Currency(5, 'USD')
        test_currency2 = Currency(10, 'USD')
        self.assertEqual(test_currency1 - test_currency2, Currency(-5.00,'USD'))

    def test_subtraction_different_code(self):
        test_currency1 = Currency(5, 'USD')
        test_currency2 = Currency(5, 'GBP')
        with self.assertRaises(DifferentCurrencyCodeError):
            test_currency1 - test_currency2

    def test_multiply_int(self):
        pass

    def test_multiply_float(self):
        pass

    def test_multiply_currency(self):
        pass

    def test_multiply_commutative(self):
        pass#self.assertTrue.(Currency() * 3 = 3 *Currency())

if __name__ == '__main__':
    unittest.main()
