import unittest


def solution(limit):
    count = 0
    while limit > 0:
        limit -= 1
        if (limit % 3 == 0) or (limit % 5 == 0):
            count += limit
            print(limit)
    return count


class MultiplesTest(unittest.TestCase):
    def test_01(self):
        self.assertEqual(solution(10), 23)
        self.assertEqual(solution(1000), 233168)
