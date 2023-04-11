import unittest

from Fibonacci import fibonacci
from FibonacciRecursivo import fibonacciRecursivo

class TestFibonacci(unittest.TestCase):

#Fibonacci

    def test_1(self):
        self.assertEqual(1, fibonacci(1))

    def test_2(self):
        self.assertEqual(1, fibonacci(2))

    def test_3(self):
        self.assertEqual(2, fibonacci(3))

    def test_4(self):
        self.assertEqual(3, fibonacci(4))

    def test_5(self):
        self.assertEqual(5, fibonacci(5))

    def test_6(self):
        self.assertEqual(8, fibonacci(6))

#Fibonacci Recursivo

    def testrecursivo_1(self):
        self.assertEqual(1, fibonacciRecursivo(1))

    def testrecusrivo_2(self):
        self.assertEqual(1, fibonacciRecursivo(2))

    def testrecursivo_3(self):
        self.assertEqual(2, fibonacciRecursivo(3))

    def testrecursivo_4(self):
        self.assertEqual(3, fibonacciRecursivo(4))

    def testrecursivo_5(self):
        self.assertEqual(5, fibonacciRecursivo(5))

    def testrecursivo_6(self):
        self.assertEqual(8, fibonacciRecursivo(6))

if __name__ == '__main__':
    unittest.main()