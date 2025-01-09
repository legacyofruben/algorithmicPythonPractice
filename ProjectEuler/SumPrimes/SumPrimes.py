import unittest
import math


def is_prime(number):
    for j in range(2, int(number**0.5) + 1):
        if number % j == 0:
            return False
    return True


def solution(input):
    count = 2
    for i in range(3, input):
        if is_prime(i):
            count += i
    return count


class Test(unittest.TestCase):
    def test_01(self):
        self.assertEqual(solution(10), 17)
