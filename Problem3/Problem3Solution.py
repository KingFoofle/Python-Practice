def reverseDiagonal(matrix):
    total = 0
    for i in range(len(matrix)):
        # Rows [0, n-1], Columns[n-1, 0]
        total += matrix[i][len(matrix) - (1 + i)]

    return total