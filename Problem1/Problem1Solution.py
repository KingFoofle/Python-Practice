def number_frequency(numList):
    numFreq = 0
    biggestNum = None

    for num in numList:
        if biggestNum is None or num > biggestNum:
            biggestNum = num
            numFreq = 1
        elif num == biggestNum:
            numFreq += 1

    return numFreq