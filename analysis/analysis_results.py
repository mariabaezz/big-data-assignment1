import pandas as pd

python_data = pd.read_csv("results/python_results.csv")
java_data = pd.read_csv("results/java_results.csv")


print("PYTHON")

for size in [50, 100, 150, 200, 250]:
    times = python_data[python_data["matrix_size"] == size]["execution_time_seconds"]

    print(size, "median:", times.median())
    print(size, "IQR:", times.quantile(0.75) - times.quantile(0.25))
    print()


print("JAVA")

for size in [50, 100, 150, 200, 250]:
    times = java_data[java_data["matrix_size"] == size]["execution_time_seconds"]

    print(size, "median:", times.median())
    print(size, "IQR:", times.quantile(0.75) - times.quantile(0.25))
    print()