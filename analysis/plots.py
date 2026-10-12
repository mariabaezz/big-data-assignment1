import pandas as pd
import matplotlib.pyplot as plt


python_data = pd.read_csv("results/python_results.csv")
java_data = pd.read_csv("results/java_results.csv")
c_data = pd.read_csv("results/c_results.csv")
memory_data = pd.read_csv("results/memory_results.csv")


sizes = [50, 100, 150, 200, 250]

python_medians = []
java_medians = []
c_medians = []


for size in sizes:

    python_times = python_data[
        python_data["matrix_size"] == size
    ]["execution_time_seconds"]

    java_times = java_data[
        java_data["matrix_size"] == size
    ]["execution_time_seconds"]

    c_times = c_data[
        c_data["matrix_size"] == size
    ]["execution_time_seconds"]

    python_medians.append(python_times.median())
    java_medians.append(java_times.median())
    c_medians.append(c_times.median())


plt.figure()

plt.plot(sizes, python_medians, marker="o", label="Python")
plt.plot(sizes, java_medians, marker="o", label="Java")
plt.plot(sizes, c_medians, marker="o", label="C")

plt.xlabel("Matrix size (n)")
plt.ylabel("Median execution time (seconds)")
plt.title("Matrix Multiplication Execution Time")

plt.legend()
plt.grid()

plt.savefig("figures/execution_time.png")

plt.show()

plt.figure()

plt.plot(sizes, python_medians, marker="o", label="Python")
plt.plot(sizes, java_medians, marker="o", label="Java")
plt.plot(sizes, c_medians, marker="o", label="C")

plt.yscale("log")

plt.xlabel("Matrix size (n)")
plt.ylabel("Median execution time (seconds, log scale)")
plt.title("Matrix Multiplication Execution Time - Log Scale")

plt.legend()
plt.grid()

plt.savefig("figures/execution_time_log.png")

plt.show()

python_memory = memory_data[
    memory_data["language"] == "Python"
]["peak_rss_bytes"] / 1_000_000

java_memory = memory_data[
    memory_data["language"] == "Java"
]["peak_rss_bytes"] / 1_000_000

c_memory = memory_data[
    memory_data["language"] == "C"
]["peak_rss_bytes"] / 1_000_000


plt.figure()

plt.plot(sizes, python_memory, marker="o", label="Python")
plt.plot(sizes, java_memory, marker="o", label="Java")
plt.plot(sizes, c_memory, marker="o", label="C")

plt.xlabel("Matrix size (n)")
plt.ylabel("Peak RSS (MB)")
plt.title("Matrix Multiplication Memory Usage")

plt.legend()
plt.grid()

plt.savefig("figures/memory_usage.png")

plt.show()