#include <stdlib.h>

void matrix_multiply(int **A, int **B, int **C, int n) {

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            C[i][j] = 0;

            for (int k = 0; k < n; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}


int **generate_matrix(int n) {

    int **matrix = malloc(n * sizeof(int *));

    for (int i = 0; i < n; i++) {
        matrix[i] = malloc(n * sizeof(int));

        for (int j = 0; j < n; j++) {
            matrix[i][j] = rand() % 10;
        }
    }

    return matrix;
}


int **create_empty_matrix(int n) {

    int **matrix = malloc(n * sizeof(int *));

    for (int i = 0; i < n; i++) {
        matrix[i] = malloc(n * sizeof(int));
    }

    return matrix;
}


void free_matrix(int **matrix, int n) {

    for (int i = 0; i < n; i++) {
        free(matrix[i]);
    }

    free(matrix);
}