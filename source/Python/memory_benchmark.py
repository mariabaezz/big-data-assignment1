import subprocess
import csv
from pathlib import Path


sizes = [50, 100, 150, 200, 250]

project_root = Path(__file__).resolve().parents[2]

python_test = project_root / "source" / "Python" / "memory_test.py"
java_folder = project_root / "source" / "java"
c_folder = project_root / "source" / "c"

results_file = project_root / "results" / "memory_results.csv"


with open(results_file, "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "language",
        "matrix_size",
        "peak_rss_bytes"
    ])


    # PYTHON
    for n in sizes:

        result = subprocess.run(
            [
                "/usr/bin/time",
                "-l",
                "python3",
                str(python_test),
                str(n)
            ],
            capture_output=True,
            text=True
        )

        for line in result.stderr.splitlines():

            if "maximum resident set size" in line:

                memory = int(line.split()[0])

                writer.writerow([
                    "Python",
                    n,
                    memory
                ])

                print(
                    "Python | Size:", n,
                    "| Peak RSS:", memory, "bytes"
                )


    # JAVA
    for n in sizes:

        result = subprocess.run(
            [
                "/usr/bin/time",
                "-l",
                "java",
                "MemoryTest",
                str(n)
            ],
            cwd=java_folder,
            capture_output=True,
            text=True
        )

        for line in result.stderr.splitlines():

            if "maximum resident set size" in line:

                memory = int(line.split()[0])

                writer.writerow([
                    "Java",
                    n,
                    memory
                ])

                print(
                    "Java | Size:", n,
                    "| Peak RSS:", memory, "bytes"
                )


    # C
    for n in sizes:

        result = subprocess.run(
            [
                "/usr/bin/time",
                "-l",
                "./memory_test",
                str(n)
            ],
            cwd=c_folder,
            capture_output=True,
            text=True
        )

        for line in result.stderr.splitlines():

            if "maximum resident set size" in line:

                memory = int(line.split()[0])

                writer.writerow([
                    "C",
                    n,
                    memory
                ])

                print(
                    "C | Size:", n,
                    "| Peak RSS:", memory, "bytes"
                )