#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    outcome = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    for a in range(len(matrix)):
        for b in range(len(matrix[a])):
            outcome[a][b] = matrix[a][b] ** 2

    return outcome
