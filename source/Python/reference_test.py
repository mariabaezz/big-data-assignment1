import csv
from pathlib import Path

import numpy as np

from matrix_multiplication import matrix_multiply


def read_matrix(filename):
    matrix = []

    with open(filename, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            matrix.append([int(value) for value in row])

    return matrix


project_root = Path(__file__).resolve().parents[2]

sizes = [50, 100, 150, 200, 250]

for n in sizes:

    A = read_matrix(project_root / "inputs" / f"A_{n}.csv")
    B = read_matrix(project_root / "inputs" / f"B_{n}.csv")

    C = [[0 for _ in range(n)] for _ in range(n)]

    matrix_multiply(A, B, C)

    A_np = np.array(A)
    B_np = np.array(B)

    C_reference = np.matmul(A_np, B_np)

    correct = np.array_equal(
        np.array(C),
        C_reference
    )

    print(
        "Size:", n,
        "| Matches NumPy:", correct
    )