import time
import csv
from pathlib import Path

from matrix_multiplication import matrix_multiply


def read_matrix(filename):
    matrix = []

    with open(filename, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            matrix.append([int(value) for value in row])

    return matrix


sizes = [50, 100, 150, 200, 250]
repetitions = 5

project_root = Path(__file__).resolve().parents[2]

results_file = project_root / "results" / "python_results.csv"


with open(results_file, "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "language",
        "matrix_size",
        "repetition",
        "execution_time_seconds",
        "checksum"
    ])

    for n in sizes:

        A = read_matrix(project_root / "inputs" / f"A_{n}.csv")
        B = read_matrix(project_root / "inputs" / f"B_{n}.csv")

        C = [[0 for _ in range(n)] for _ in range(n)]

        for repetition in range(1, repetitions + 1):

            start = time.perf_counter()

            C = matrix_multiply(A, B, C)

            end = time.perf_counter()

            elapsed_time = end - start

            checksum = sum(sum(row) for row in C)

            writer.writerow([
                "Python",
                n,
                repetition,
                elapsed_time,
                checksum
            ])


            print(
                "Size:", n,
                "| Repetition:", repetition,
                "| Time:", elapsed_time, "seconds",
                "| Checksum:", checksum
            )