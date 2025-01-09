import math
import unittest


def solution(input):
    for i in range(0, 1000, 1):
        pytha = math.sqrt((i + 1) ** 2 + (i + 2) ** 2)
        print(f"a: {(i + 1)}, + b: {(i + 2)}, c: {pytha} sum: {pytha + (i + 1) + (i + 2)}")
        if (pytha + (i + 1) + (i + 2)) == input:
            break
        #     print(f"a: {a}, + b: {b}, c: {c} prod: {a*b*c}")
    return 0


class Test(unittest.TestCase):
    def test_01(self):
        self.assertEqual(solution(1000), 2)
