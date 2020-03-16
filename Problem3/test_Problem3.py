from unittest import TestCase

import Problem3


class Test(TestCase):
    def test_reverse_diagonal(self):
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

        case1 = Problem3.reverseDiagonal(matrix1)
        case2 = Problem3.reverseDiagonal(matrix2)
        case3 = Problem3.reverseDiagonal(matrix3)
        case4 = Problem3.reverseDiagonal(matrix4)

        # What "assert" functions do, is simple. If they DON'T get the value you expect, it RAISES an error :)
        self.assertIsNotNone(case1, "Your function is not returning a value")
        self.assertEquals(15, case1, "Your function is not returning the correct value")
        self.assertEqual(0, case2, "The Matrix is empty, the value should be 0")

        self.assertEqual(19, case3, "Your function is not returning the correct value")
        self.assertEqual(80.3, case4, "Your function is not returning the correct value")
