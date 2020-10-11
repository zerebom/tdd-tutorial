import unittest

from dollar import Dollor

class MoneyTest(unittest.TestCase):
    def test_multiplication(self):
        five = Dollor(5)
        five.times(2)
        assert 10 == five.amount

if __name__ == "__main__":
    unittest.main()