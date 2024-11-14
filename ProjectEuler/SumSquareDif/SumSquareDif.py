import unittest


def solution(range):
    sum_num = 0
    sum_with_square = 0
    while range > 0:
        sum_num += range
        sum_with_square += range * range
        range -= 1
    sum_num = sum_num * sum_num
    print(f"{sum_num} - {sum_with_square}")
    return sum_num - sum_with_square


class Test(unittest.TestCase):
    def test_01(self):
        self.assertEqual(solution(10), 2640)

    def test_02(self):
        self.assertEqual(solution(100), 25164150)
