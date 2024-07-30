import unittest
import time

# https://app.codility.com/programmers/lessons/1-iterations/binary_gap/


def solution(input):
    # print(bin(input)[2:])
    count = 0
    _max = 0
    for char in bin(input)[2:]:
        if char == '0':
            count += 1
        else:
            _max = max(count, _max)
            count = 0

    return _max


pass


def solution_2(input):
    # print(bin(input)[2:].split('1'))
    _max = 0
    for item in bin(input)[2:].split('1'):
        _max = max(_max,len(item))
    return _max


pass


class BinaryGapTest(unittest.TestCase):
    def test_01(self):
        self.assertEqual(solution(529), 4)
        self.assertEqual(solution(1041), 5)
        start_time = time.time()
        self.assertEqual(solution(10000000000000000000000000000000000000000000000), 7)
        end_time = time.time()
        print(end_time - start_time)
        pass

    def test_02(self):
        self.assertEqual(solution_2(529), 4)
        self.assertEqual(solution_2(1041), 5)
        start_time = time.time()
        self.assertEqual(solution(10000000000000000000000000000000000000000000000), 7)
        end_time = time.time()
        print(end_time - start_time)
        pass


pass
