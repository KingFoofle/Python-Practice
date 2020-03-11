from unittest import TestCase

import Problem1


class Test(TestCase):
    def test_number_frequency(self):
        case1 = Problem1.number_frequency([1, 1, 1])
        case2 = Problem1.number_frequency([])  # Empty list
        case3 = Problem1.number_frequency([1, 1, 4, 7, 3, 7, 3, 3, 6, 3, 5, 6, 8, 8])
        case4 = Problem1.number_frequency([1])
        case5 = Problem1.number_frequency([-1, 4, 5, 8, -2, 6, 4, 6, 7, 4, 3, 5, 9, 7, 8, 2, 1, 4, -4, 6, 9, 9])
        self.assertIsNotNone(case1, "Your function is not returning a value")
        self.assertEqual(3, case1, "Your function did not return the correct number")
        self.assertEqual(0, case2, "Your function did not return the correct number")
        self.assertEqual(2, case3, "Your function did not return the correct number")
        self.assertEqual(1, case4, "Your function did not return the correct number")
        self.assertEqual(3, case5, "Your function did not return the correct number")
