#include <stdio.h>
#include <stdlib.h>

void matrix_multiply(int **A, int **B, int **C, int n);
int **create_empty_matrix(int n);
void free_matrix(int **matrix, int n);


int **read_matrix(const char *filename, int n) {

    FILE *file = fopen(filename, "r");

    int **matrix = create_empty_matrix(n);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {

            if (j < n - 1) {
                fscanf(file, "%d,", &matrix[i][j]);
            } else {
                fscanf(file, "%d", &matrix[i][j]);
            }
        }
    }

    fclose(file);

    return matrix;
}


int main(int argc, char *argv[]) {

    int n = atoi(argv[1]);

    char filenameA[100];
    char filenameB[100];

    sprintf(filenameA, "../../inputs/A_%d.csv", n);
    sprintf(filenameB, "../../inputs/B_%d.csv", n);

    int **A = read_matrix(filenameA, n);
    int **B = read_matrix(filenameB, n);
    int **C = create_empty_matrix(n);

    matrix_multiply(A, B, C, n);

    free_matrix(A, n);
    free_matrix(B, n);
    free_matrix(C, n);

    return 0;
}