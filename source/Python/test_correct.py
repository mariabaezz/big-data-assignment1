from matrix_multiplication import matrix_multiply


# Test 1: Known matrices
A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

expected = [
    [19, 22],
    [43, 50]
]

result = matrix_multiply(A, B)

print("Known matrices test:", result == expected)


# Test 2: Identity matrix
A = [
    [1, 0, 4],
    [3, 3, 2],
    [1, 8, 1]
]

I = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

result = matrix_multiply(A, I)

print("Identity matrix test:", result == A)


# Test 3: Zero matrix
Z = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

expected_zero = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

result = matrix_multiply(A, Z)

print("Zero matrix test:", result == expected_zero)