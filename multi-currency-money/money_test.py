import unittest

from dollar import Dollor

class MoneyTest(unittest.TestCase):
    def test_multiplication(self):
        five = Dollor(5)
        product = five.times(2)
        self.assertEqual(10, product.amount)
        product = five.times(3)
        self.assertEqual(15, product.amount)

    def test_equality(self):
        # Value Objectにするため、等価性のテストを行う
        self.assertTrue(Dollor(5).equals(Dollor(5)))
        self.assertFalse(Dollor(5).equals(Dollor(6)))

if __name__ == "__main__":
    unittest.main()