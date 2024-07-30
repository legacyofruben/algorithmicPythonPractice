import unittest


def solution(limit):
    n1 = 1
    n2 = 2
    next = 0
    sum = 2

    while sum < limit:
        next = n1 + n2
        print(next)
        if (next % 2) == 0:
            sum += next
            print(f" {sum}")

        print()
        n1 = n2
        n2 = next

    return sum


class EvenFibonacciTest(unittest.TestCase):
    def test_01(self):
        self.assertEqual(solution(4000000), 4613732)
