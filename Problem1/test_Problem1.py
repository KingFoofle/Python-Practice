from unittest import TestCase

import Problem1


class Test(TestCase):
    def test_number_frequency(self):
        case1 = Problem1.number_frequency([1, 1, 1])
        case2 = Problem1.number_frequency([])  # Empty list
        case3 = Problem1.number_frequency([1, 1, 4, 7, 3, 7, 3, 3, 6, 3, 5, 6, 8, 8])
        case4 = Problem1.number_frequency([1])
        self.assertEqual(3, case1, "Your function did not return the correct number")
        self.assertEqual(0, case2, "Your function did not return the correct number")
        self.assertEqual(2, case3, "Your function did not return the correct number")
        self.assertEqual(1, case4, "Your function did not return the correct number")
