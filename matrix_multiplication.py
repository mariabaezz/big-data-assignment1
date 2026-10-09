import random


def matrix_multiply(A, B):
    n = len(A)

    C = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C


def generate_matrix(n):
    return [
        [random.randint(0, 9) for _ in range(n)]
        for _ in range(n)
    ]