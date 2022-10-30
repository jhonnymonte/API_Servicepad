import unittest
from fibonacci import fibonacci_series

class Test_fibonacci(unittest.TestCase):
    def test_fib_1_equals_1():
        assert fibonacci_series(1) == 1

    def test_fib_2_equals_1():
         assert fibonacci_series(2) == 1

    def test_fib_6_equals_8():
         assert fibonacci_series(6) == 8


	