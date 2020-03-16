from unittest import TestCase

import Problem2


class Test(TestCase):
    # I used a class called unittest, which tests your functions
    def test_diagonal_sum(self):
        matrix1 = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]

        matrix2 = []

        matrix3 = [
            [11, 2, 4],
            [4, 5, 6],
            [10, 8, -12]
        ]

        matrix4 = [
            [1.0, 30, 40],
            [0, 40.3, 23],
            [0, 0, 100]
        ]

        case1 = Problem2.diagonalSum(matrix1)
        case2 = Problem2.diagonalSum(matrix2)
        case3 = Problem2.diagonalSum(matrix3)
        case4 = Problem2.diagonalSum(matrix4)

        # What "assert" functions do, is simple. If they DON'T get the value you expect, it RAISES an error :)
        self.assertIsNotNone(case1, "Your function is not returning a value")
        self.assertEquals(15, case1, "Your function is not returning the correct value")
        self.assertEqual(0, case2, "The Matrix is empty, the value should be 0")

        self.assertEqual(4, case3, "Your function is not returning the correct value")
        self.assertEqual(141.3, case4, "Your function is not returning the correct value")
