import unittest

from dollar import Dollor,Franc

class MoneyTest(unittest.TestCase):
    def test_multiplication(self):
        five = Dollor(5)
        self.assertTrue(Dollor(10).equals(five.times(2)))
        self.assertTrue(Dollor(15).equals(five.times(3)))

    def test_franc_multiplication(self):
        five = Franc(5)
        self.assertTrue(Franc(10).equals(five.times(2)))
        self.assertTrue(Franc(15).equals(five.times(3)))

    def test_equality(self):
        # Value Objectにするため、等価性のテストを行う
        self.assertTrue(Dollor(5).equals(Dollor(5)))
        self.assertFalse(Dollor(5).equals(Dollor(6)))
        self.assertFalse(Dollor(5).equals(Franc(5)))

if __name__ == "__main__":
    unittest.main()