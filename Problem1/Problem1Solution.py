def number_frequency(numList):
    if len(numList) == 0:
        return 0
    bignumfrequency = 0
    biggestnumber = sorted(numList, reverse=True)[0]
    for number in sorted(numList, reverse=True):
        if number == biggestnumber:
            bignumfrequency += 1

        if number > biggestnumber:
            break  # End of biggest number count

    return bignumfrequency