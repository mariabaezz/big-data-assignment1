# Assignment 1 - Basic Matrix Multiplication

Big Data - Academic Year 2026-2027  
Degree in Data Science and Engineering  
Universidad de Las Palmas de Gran Canaria

---

## Objective

The objective of this assignment is to compare basic dense matrix multiplication implementations in Python, Java and C.

The same standard triple-loop O(n³) algorithm is implemented in the three languages.

The experiment studies how matrix size affects:

- Execution time
- Memory usage

The implementations use the same input matrices in order to make the comparison reproducible.

---

## Project Structure

```text
Assignment1/
├── analysis/
│   ├── analysis_results.py
│   └── plots.py
│
├── figures/
│   ├── execution_time.png
│   ├── execution_time_log.png
│   └── memory_usage.png
│
├── inputs/
│   ├── generate_inputs.py
│   ├── A_50.csv
│   ├── B_50.csv
│   ├── ...
│   ├── A_250.csv
│   └── B_250.csv
│
├── report/
│   ├── main.tex
│   └── references.bib
│
├── results/
│   ├── python_results.csv
│   ├── java_results.csv
│   ├── c_results.csv
│   └── memory_results.csv
│
├── source/
│   ├── Python/
│   │   ├── matrix_multiplication.py
│   │   ├── benchmark.py
│   │   ├── test_correctness.py
│   │   ├── memory_test.py
│   │   └── memory_benchmark.py
│   │
│   ├── java/
│   │   ├── MatrixMultiplication.java
│   │   ├── Benchmark.java
│   │   ├── TestCorrectness.java
│   │   └── MemoryTest.java
│   │
│   └── c/
│       ├── matrix_multiplication.c
│       ├── benchmark.c
│       ├── test_correctness.c
│       └── memory_test.c
│
├── environment.txt
└── README.md
```

---

## Experimental Inputs

The tested matrix sizes are:

```text
50, 100, 150, 200, 250
```

Input matrices contain integer values between 0 and 9.

The matrices are generated once using Python with random seed:

```text
42
```

The generated matrices are saved as CSV files in the `inputs/` directory.

Python, Java and C read the same CSV files, so all three implementations use the same logical input matrices.

To regenerate the input files, run from the project root:

```bash
python3 inputs/generate_inputs.py
```

---

## Correctness Tests

Before benchmarking, the implementations are tested using:

- Matrices with a known multiplication result
- Identity matrix
- Zero matrix

### Python

From the project root:

```bash
python3 source/Python/test_correctness.py
```

### Java

```bash
cd source/java
javac MatrixMultiplication.java TestCorrectness.java
java TestCorrectness
cd ../..
```

### C

```bash
cd source/c
clang matrix_multiplication.c test_correctness.c -o test_correctness
./test_correctness
cd ../..
```

All correctness tests should return `true`.

---

## Implementation Details

All three implementations use the same straightforward triple-loop matrix multiplication algorithm with the loop order i -> j -> k.

The algorithm performs O(n^3) arithmetic operations for two n x n dense matrices.

Python stores the matrices as lists of lists of Python integers.

Java uses two-dimensional int arrays (int[][]).

C uses dynamically allocated integer matrices through pointers.

Java and C use fixed-width integer representations provided by their respective implementations, while Python integers have different runtime storage characteristics.

These language-specific storage differences are unavoidable and are considered when interpreting the memory results.

No optimized matrix multiplication libraries such as NumPy, BLAS or similar libraries are used for the multiplication itself.

The implementations are sequential. No explicit multithreading or parallel execution is used in Assignment 1.

---


## Runtime Benchmark

For each language, five measured repetitions are performed for every matrix size.

Input loading is excluded from the timed region. Only the matrix multiplication operation is measured.

### Python

Python uses:

```text
time.perf_counter()
```

Run from the project root:

```bash
python3 source/Python/benchmark.py
```

Results are stored in:

```text
results/python_results.csv
```

### Java

Java uses:

```text
System.nanoTime()
```

One untimed multiplication is performed before the measured repetitions as JVM warm-up.

Run:

```bash
cd source/java
javac MatrixMultiplication.java Benchmark.java
java Benchmark
cd ../..
```

Results are stored in:

```text
results/java_results.csv
```

### C

C uses:

```text
CLOCK_MONOTONIC
```

The program is compiled with optimisation level `-O2`.

Run:

```bash
cd source/c
clang -O2 matrix_multiplication.c benchmark.c -o benchmark
./benchmark
cd ../..
```

Results are stored in:

```text
results/c_results.csv
```

---

## Statistical Analysis

For every matrix size and language, the analysis reports:

- Median execution time
- Interquartile range (IQR)

Run from the project root:

```bash
python3 analysis/analysis_results.py
```

The analysis uses `pandas`.

---

## Figures

The plots are generated using `matplotlib`.

Run:

```bash
python3 analysis/plots.py
```

The following figures are generated:

```text
figures/execution_time.png
figures/execution_time_log.png
figures/memory_usage.png
```

The logarithmic execution-time plot is included because the large difference between Python and the compiled/JVM implementations makes Java and C difficult to distinguish on a linear scale.

---

## Memory Benchmark

Memory usage is measured using Peak Resident Set Size (Peak RSS).

The measurement uses the macOS command `/usr/bin/time -l`.

The memory benchmark automatically executes the different matrix sizes for Python, Java and C, extracts the maximum resident set size, and stores the results in a common CSV file.

### Python

Python does not require compilation.

The memory test program is located at:

source/Python/memory_test.py

The complete memory benchmark is launched through:

python3 source/Python/memory_benchmark.py

This script internally executes the Python memory test for every matrix size using `/usr/bin/time -l`.

### Java

Before running the complete memory benchmark, compile the Java memory test:

cd source/java
javac MatrixMultiplication.java MemoryTest.java
cd ../..

### C

Before running the complete memory benchmark, compile the C memory test with optimization level `-O2`:

cd source/c
clang -O2 matrix_multiplication.c memory_test.c -o memory_test
cd ../..

### Run the complete memory benchmark

From the project root, run:

python3 source/Python/memory_benchmark.py

This executes the memory tests for Python, Java and C for all tested matrix sizes.

Results are stored in:

results/memory_results.csv

The reported Peak RSS represents the memory usage of the complete process, not only the memory occupied by the matrices. Therefore, runtime overhead such as the Python interpreter and the Java Virtual Machine is also included.

The memory measurement script is specific to macOS because it uses `/usr/bin/time -l`.
---

## Experimental Environment

The experiments were executed on:

- MacBook Pro
- Apple M4
- 10 CPU cores
  - 4 Performance cores
  - 6 Efficiency cores
- 10 logical processors
- 16 GB RAM
- macOS 26.3.1
- ARM64 architecture

Software:

- Python 3.13.0
- OpenJDK 25.0.2
- javac 25.0.2
- Apple Clang 21.0.0
- pandas: 3.0.0
- matplotlib: 3.10.8

Additional environment information is available in:

```text
environment.txt
```

---

## Reproducibility

The general experiment can be reproduced in the following order:

1. Generate the shared input matrices.
2. Run correctness tests.
3. Run the Python, Java and C runtime benchmarks.
4. Run the memory benchmark.
5. Run the statistical analysis.
6. Generate the plots.

Raw measurements are preserved in the `results/` directory.

The source code, experimental inputs, raw results and analysis scripts are included in this repository.