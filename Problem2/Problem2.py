import test_Problem2


# Given a 2D Array, return the sum of the DIAGONAL numbers

# For example, [
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]    <--- This is a 3x3 matrix.
# ]
# The diagonal would be 1, 5, 9 = 15

# HINT: Assume that the matrix will always be nxn

def diagonalSum(matrix):
    pass


# ------- DO NOT EDIT THE CODE BELOW -------

def main():
    try:
        test_Problem2.Test().test_diagonal_sum()

    except AssertionError as e:
        print(e)
        print("Your code must pass all tests to succeed. Try again!")

    else:
        print("Congratulations! You passed!")
        print("\nTry another version of this problem at:")
        print("https://www.hackerrank.com/challenges/diagonal-difference/problem")
        print("------------------------------------")


if __name__ == "__main__":
    main()