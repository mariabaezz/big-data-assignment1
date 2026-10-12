import pandas as pd

python_data = pd.read_csv("results/python_results.csv")
java_data = pd.read_csv("results/java_results.csv")
c_data = pd.read_csv("results/c_results.csv")

sizes = [50, 100, 150, 200, 250]

summary_rows = []


print("PYTHON")

for size in sizes:
    times = python_data[
        python_data["matrix_size"] == size
    ]["execution_time_seconds"]

    median = times.median()
    iqr = times.quantile(0.75) - times.quantile(0.25)

    print(size, "median:", median)
    print(size, "IQR:", iqr)
    print()

    summary_rows.append([
        "Python",
        size,
        median,
        iqr
    ])


print("JAVA")

for size in sizes:
    times = java_data[
        java_data["matrix_size"] == size
    ]["execution_time_seconds"]

    median = times.median()
    iqr = times.quantile(0.75) - times.quantile(0.25)

    print(size, "median:", median)
    print(size, "IQR:", iqr)
    print()

    summary_rows.append([
        "Java",
        size,
        median,
        iqr
    ])


print("C")

for size in sizes:
    times = c_data[
        c_data["matrix_size"] == size
    ]["execution_time_seconds"]

    median = times.median()
    iqr = times.quantile(0.75) - times.quantile(0.25)

    print(size, "median:", median)
    print(size, "IQR:", iqr)
    print()

    summary_rows.append([
        "C",
        size,
        median,
        iqr
    ])


summary = pd.DataFrame(
    summary_rows,
    columns=[
        "language",
        "matrix_size",
        "median_time_seconds",
        "iqr_seconds"
    ]
)

summary.to_csv(
    "results/summary_time.csv",
    index=False
)

print("Summary saved to results/summary_time.csv")