#!/usr/bin/python
import unittest
import level
import rubik
import time
import sys

class TestLevel(unittest.TestCase):
    f = [ 1, 9, 54, 321, 1847, 9992, 50136, 227536, 870072, 1887748, 623800, 2644,0]
    q = [1,6,27,120,534,2256,8969, 33058,114149, 360508,930588,1350852,782536,90280,276,0]
    
    def testLevel0(self):
        self.level_test(0)

    def testLevel1(self):
        self.level_test(1)

    def testLevel2(self):
        self.level_test(2)

    def testLevel3(self):
        self.level_test(3)

    def testLevel4(self):
        self.level_test(4)

    def testLevel5(self):
        self.level_test(5)

    def testLevel6(self):
        self.level_test(6)

    def testLevel7(self):
        self.level_test(7)

    def testLevel8(self):
        self.level_test(8)
        
### It is recommended that you use a machine with 1GB of RAM if you
### want to run the following tests.
#    def testLevel9(self):
#        self.level_test(9)

#    def testlevel10(self):
#        self.level_test(10)

#     def testlevel11(self):
#         self.level_test(11)

    def level_test(self, l):
        start_time = time.time()
        ans = level.positions_at_level(l)
        end_time = time.time()

        self.assertEqual(ans, self.f[l])
        print 'time for level', l, end_time - start_time, 'seconds'

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLevel)
    unittest.TextTestRunner(verbosity=2).run(suite)
