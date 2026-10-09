import random
import time
import csv
from pathlib import Path

from matrix_multiplication import matrix_multiply, generate_matrix


random.seed(42)

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
        "execution_time_seconds"
    ])

    for n in sizes:
        A = generate_matrix(n)
        B = generate_matrix(n)

        for repetition in range(1, repetitions + 1):

            start = time.perf_counter()

            C = matrix_multiply(A, B)

            end = time.perf_counter()

            elapsed_time = end - start

            writer.writerow([
                "Python",
                n,
                repetition,
                elapsed_time
            ])

            print(
                "Size:", n,
                "| Repetition:", repetition,
                "| Time:", elapsed_time, "seconds"
            )