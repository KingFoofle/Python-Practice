def solution(matrix):
    total = 0
    for i in range(len(matrix)):
        # nxn matrix
        total += matrix[i][i]

    return total