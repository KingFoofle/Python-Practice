import test_Problem1


# Problem 1:
# Make a function that takes an array of integers and returns the frequency of the highest number in the array
# For example: [1,2,2,3,3,3,10,10] should return 2, since 10 repeats 2 times
# Skills needed: Loops, Sorting, If statements, Return

def number_frequency(numList):
    pass


# ------- DO NOT EDIT THE CODE BELOW -------

if __name__ == "__main__":
    try:
        test_Problem1.Test().test_number_frequency()

    except AssertionError as e:
        print(e)
        print("Your code must pass all tests to succeed. Try again!")

    else:
        print("Congratulations! You passed!")
        print("\nTry another version of this problem at:")
        print("https://www.hackerrank.com/challenges/birthday-cake-candles/problem")
