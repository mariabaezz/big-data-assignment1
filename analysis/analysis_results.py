import pandas as pd
import math

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


# Normalize median execution time by n^3
summary["normalized_time"] = (
    summary["median_time_seconds"] /
    (summary["matrix_size"] ** 3)
)


summary.to_csv(
    "results/summary_time.csv",
    index=False
)


print("Summary saved to results/summary_time.csv")


print("\nLOG-LOG SLOPE")

for language in ["Python", "Java", "C"]:

    language_data = summary[
        summary["language"] == language
    ].sort_values("matrix_size")

    n1 = language_data.iloc[0]["matrix_size"]
    n2 = language_data.iloc[-1]["matrix_size"]

    t1 = language_data.iloc[0]["median_time_seconds"]
    t2 = language_data.iloc[-1]["median_time_seconds"]

    slope = math.log(t2 / t1) / math.log(n2 / n1)

    print(language, "slope:", slope)