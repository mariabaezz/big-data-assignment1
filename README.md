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
## Research Question and Hypothesis

The research question is:

How does the execution time and memory usage of the same basic dense matrix multiplication algorithm differ when implemented in Python, Java and C on the same hardware and using the same input matrices?

The hypothesis is that execution time will increase approximately according to the cubic growth of the standard matrix multiplication algorithm as matrix size increases.

It is also expected that the three implementations will show different execution times and memory usage because of differences in their runtime environments, memory representations and execution models. These results are specific to the tested implementations and experimental environment and are not intended as universal claims about the programming languages.


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
│   ├── memory_results.csv
|   └── summary_time.csv
│
├── source/
│   ├── Python/
│   │   ├── matrix_multiplication.py
│   │   ├── benchmark.py
│   │   ├── test_correct.py
│   │   ├── reference_test.py
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
python3 source/Python/test_correct.py
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

### Reference Validation

In addition to the basic correctness tests, the Python implementation is compared against NumPy as a trusted reference implementation.

Run from the project root:

```bash
python3 source/Python/reference_test.py
```

The reference test uses the same CSV input matrices used in the benchmarks and compares the complete multiplication result with `numpy.matmul`.

All tested matrix sizes (50, 100, 150, 200 and 250) matched the NumPy reference.

The runtime benchmarks also calculate a checksum of the resulting matrix after the timed region. For every matrix size, the checksum is identical in Python, Java and C, providing an additional cross-language correctness check.

---

## Implementation Details

All three implementations use the same straightforward triple-loop matrix multiplication algorithm with the loop order i -> j -> k.

The algorithm performs O(n^3) arithmetic operations for two n x n dense matrices.

Python stores the matrices as lists of lists of Python integers.

Java uses two-dimensional int arrays (`int[][]`).

C uses dynamically allocated integer matrices through pointers.

Java stores matrix values using 32-bit signed `int` values. C uses the `int` type, which is 32 bits on the tested platform. Python uses arbitrary-precision integer objects with different runtime storage characteristics.

With input values between 0 and 9 and a maximum tested matrix size of 250, the maximum possible value of a single output element is 250 × 9 × 9 = 20,250, which is well within the integer range used by Java and C.

These language-specific storage differences are considered when interpreting the memory results.

No optimized matrix multiplication libraries such as NumPy, BLAS or similar libraries are used for the benchmarked multiplication itself.

NumPy is used only as a trusted reference implementation for correctness validation.

The implementations are sequential. No explicit multithreading or parallel execution is used in Assignment 1.

---

## Runtime Benchmark

For each language, five measured repetitions are performed for every matrix size.

Input loading and allocation of the output matrix `C` are excluded from the timed region.

Inside the timed region, each output element is initialized with `C[i][j] = 0` and the standard triple-loop multiplication is performed.

After the timer stops, the resulting matrix is consumed by calculating a checksum. The checksum calculation is therefore not included in the measured execution time.

The checksum is stored together with every runtime measurement in the result CSV files. For each matrix size, the checksum is identical across Python, Java and C.

### Python

Python uses:

`time.perf_counter()`

Run from the project root:
```bash
python3 source/Python/benchmark.py
```

Results are stored in:

`results/python_results.csv`


### Java

Java uses:

`System.nanoTime()`

Three untimed multiplication executions are performed for each matrix size before the five measured repetitions as JVM warm-up.

Run:

```bash
cd source/java
javac MatrixMultiplication.java Benchmark.java
java Benchmark
cd ../..
```

Results are stored in:

`results/java_results.csv`

### C

C uses:

`CLOCK_MONOTONIC`

The program is compiled with optimisation level `-O2`.

Run:

```bash
cd source/c
clang -O2 matrix_multiplication.c benchmark.c -o benchmark
./benchmark
cd ../..
```

Results are stored in:

`results/c_results.csv`

### Fixed Execution Settings

The following settings are kept fixed during the final experiments:

- Python: CPython 3.13.0
- Java: OpenJDK 25.0.2
- Java warm-up: 3 untimed executions per matrix size
- C compiler: Apple Clang 21.0.0
- C compilation optimization: `-O2`
- Five measured runtime repetitions per language and matrix size
- Same loop order: `i -> j -> k`
- Same shared CSV input matrices
- No explicit parallelism or multithreading in the matrix multiplication code

Java may internally use JVM services such as JIT compilation or garbage collection, while Python includes interpreter overhead and C is compiled ahead of time. These differences are part of the execution environments and are considered when interpreting the results.

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

The script also generates the summary file:

`results/summary_time.csv`

This file contains the median execution time and IQR for every language and matrix size and is used to prepare the result tables in the report.

---

## Experimental Scope and Limits

The final runtime experiment uses matrix sizes from 50 to 250.

A practical execution-time budget of 5 seconds per individual multiplication and a Peak RSS memory budget of 1 GB are used as feasibility limits for the final experiment.

All tested configurations remained within these limits.

The largest tested and attempted matrix size in the final experiment is:

n = 250

No larger configuration is reported as a failure because sizes above 250 were not attempted in the final experiment.

Therefore, n = 250 should be interpreted as the largest tested size in this study, not as the maximum matrix size that the machine or languages can process.

---

## Figures

The plots are generated using `matplotlib`.

Run:

```bash
python3 analysis/plots.py
```

The following figures are generated:

- figures/execution_time.png
- figures/execution_time_log.png
- figures/memory_usage.png

The logarithmic execution-time plot is included because the large difference between Python and the compiled/JVM implementations makes Java and C difficult to distinguish on a linear scale.

---

## Memory Benchmark

Memory usage is measured using Peak Resident Set Size (Peak RSS).

The measurement uses the macOS command `/usr/bin/time -l`.

The memory benchmark automatically executes the different matrix sizes for Python, Java and C, extracts the maximum resident set size, and stores the results in a common CSV file.

### Python

Python does not require compilation.

The memory test program is located at:

`source/Python/memory_test.py`

The complete memory benchmark is launched through:

```bash
python3 source/Python/memory_benchmark.py
```

This script internally executes the Python memory test for every matrix size using `/usr/bin/time -l`.

### Java

Before running the complete memory benchmark, compile the Java memory test:

```bash
cd source/java
javac MatrixMultiplication.java MemoryTest.java
cd ../..
```

### C

Before running the complete memory benchmark, compile the C memory test with optimization level `-O2`:

```bash
cd source/c
clang -O2 matrix_multiplication.c memory_test.c -o memory_test
cd ../..
```

### Run the Complete Memory Benchmark

From the project root, run:

```bash
python3 source/Python/memory_benchmark.py
```

This executes the memory tests for Python, Java and C for all tested matrix sizes.

Results are stored in:

`results/memory_results.csv`

The reported Peak RSS represents the memory usage of the complete process, not only the memory occupied by the matrices. Therefore, runtime overhead such as the Python interpreter and the Java Virtual Machine is also included.

The memory measurement script is specific to macOS because it uses `/usr/bin/time -l`.

One Peak RSS measurement is recorded for each language and matrix size. Unlike the runtime experiment, the memory results are therefore presented as individual process-level measurements rather than as median and IQR statistics.

Runtime and memory results are analysed separately because they represent different performance metrics.
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
## Use of Generative AI

ChatGPT (OpenAI) was used as a support tool during the assignment for explaining concepts, planning the experimental workflow, assisting with code development and debugging, and revising the English wording of the documentation.

All programs were reviewed and executed by the student. Experimental measurements were generated locally on the hardware described above, and the reported results were checked against the raw CSV files. NumPy was used only as a trusted correctness reference and not as part of the benchmarked matrix multiplication implementations.

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