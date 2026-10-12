import csv
import sys
from pathlib import Path

from matrix_multiplication import matrix_multiply


def read_matrix(filename):
    matrix = []

    with open(filename, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            matrix.append([int(value) for value in row])

    return matrix


n = int(sys.argv[1])

project_root = Path(__file__).resolve().parents[2]

A = read_matrix(project_root / "inputs" / f"A_{n}.csv")
B = read_matrix(project_root / "inputs" / f"B_{n}.csv")

C = matrix_multiply(A, B)