#!/usr/bin/python
import unittest
import profile
import pstats
from peak_finder_2d import *
from utils_2d import *

def test(filename):
        # Check correctness
        global n
        global matrix
        (n, matrix) = read_input(filename)
        (x_peak_quick, y_peak_quick) = quick_find_2d_peak(matrix, 0, n - 1, 0, n - 1)
        isCorrect = is_a_peak(n, matrix, (x_peak_quick, y_peak_quick))
        
        # # Check speed
        # profile.run('quick_find_2d_peak(matrix, 0, n - 1, 0, n - 1)', '2d_quick_stats')
        # profile.run('medium_find_2d_peak(matrix, 0, n - 1, 0, n - 1)', '2d_med_stats')
        # 
        # p1 = pstats.Stats('2d_quick_stats')
        # quick_time = p1.total_tt
        # p2 = pstats.Stats('2d_med_stats')
        # medium_time = p2.total_tt
        # isFastEnough = medium_time > 2 * quick_time
        
        # return isCorrect and isFastEnough
        return isCorrect

# Testing framework for the 2D case of the peak finding algorithm.
class TestPS1Part2(unittest.TestCase):

    def setUp(self):
        pass

    def test1(self):
                doesPass = test("1_small_random.txt")
                self.assertTrue(doesPass)
                
    def test2(self):
                doesPass = test("2_medium_random.txt")
                self.assertTrue(doesPass)

    def test3(self):
                doesPass = test("3_big_random.txt")
                self.assertTrue(doesPass)

    def test4(self):
                doesPass = test("4_two_mountains.txt")
                self.assertTrue(doesPass)

    def test5(self):
                doesPass = test("5_20_mountains.txt")
                self.assertTrue(doesPass)

    def test6(self):
                doesPass = test("6_100_mountains.txt")
                self.assertTrue(doesPass)

    def test7(self):
                doesPass = test("7_small_spiral.txt")
                self.assertTrue(doesPass)

    def test8(self):
                doesPass = test("8_medium_spiral.txt")
                self.assertTrue(doesPass)

    def test9(self):
                doesPass = test("9_big_spiral.txt")
                self.assertTrue(doesPass)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPS1Part2)
    unittest.TextTestRunner(verbosity=2).run(suite)