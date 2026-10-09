import pandas as pd

data = pd.read_csv("results/python_results.csv")

size_50 = data[data["matrix_size"] == 50]["execution_time_seconds"]
size_100 = data[data["matrix_size"] == 100]["execution_time_seconds"]
size_150 = data[data["matrix_size"] == 150]["execution_time_seconds"]
size_200 = data[data["matrix_size"] == 200]["execution_time_seconds"]
size_250 = data[data["matrix_size"] == 250]["execution_time_seconds"]

print("50 median:", size_50.median())
print("50 IQR:", size_50.quantile(0.75) - size_50.quantile(0.25))
print()

print("100 median:", size_100.median())
print("100 IQR:", size_100.quantile(0.75) - size_100.quantile(0.25))
print()

print("150 median:", size_150.median())
print("150 IQR:", size_150.quantile(0.75) - size_150.quantile(0.25))
print()

print("200 median:", size_200.median())
print("200 IQR:", size_200.quantile(0.75) - size_200.quantile(0.25))
print()

print("250 median:", size_250.median())
print("250 IQR:", size_250.quantile(0.75) - size_250.quantile(0.25))