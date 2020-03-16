import test_Problem3

# Calculate the sum of the REVERSE diagonal of a nxn matrix

def reverseDiagonal(matrix):
    pass


# ------- DO NOT EDIT THE CODE BELOW -------

def main():
    try:
        test_Problem3.Test().test_reverse_diagonal()

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