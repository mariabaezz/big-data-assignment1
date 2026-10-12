#include <stdio.h>
#include <stdlib.h>
#include <time.h>

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


double current_time() {

    struct timespec time;

    clock_gettime(CLOCK_MONOTONIC, &time);

    return time.tv_sec + time.tv_nsec / 1000000000.0;
}


int main() {

    int sizes[] = {50, 100, 150, 200, 250};
    int repetitions = 5;

    FILE *file = fopen("../../results/c_results.csv", "w");

    fprintf(
        file,
        "language,matrix_size,repetition,execution_time_seconds,checksum\n"
    );

    for (int s = 0; s < 5; s++) {

        int n = sizes[s];

        char filenameA[100];
        char filenameB[100];

        sprintf(filenameA, "../../inputs/A_%d.csv", n);
        sprintf(filenameB, "../../inputs/B_%d.csv", n);

        int **A = read_matrix(filenameA, n);
        int **B = read_matrix(filenameB, n);
        int **C = create_empty_matrix(n);

        for (int repetition = 1; repetition <= repetitions; repetition++) {

            double start = current_time();

            matrix_multiply(A, B, C, n);

            double end = current_time();

            double elapsed_time = end - start;

            long long checksum = 0;

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    checksum += C[i][j];
                }
            }

            printf(
                "Size: %d | Repetition: %d | Time: %f seconds | Checksum: %lld\n",
                n,
                repetition,
                elapsed_time,
                checksum
            );

            fprintf(
                file,
                "C,%d,%d,%f,%lld\n",
                n,
                repetition,
                elapsed_time,
                checksum
            );
        }

        free_matrix(A, n);
        free_matrix(B, n);
        free_matrix(C, n);
    }

    fclose(file);

    return 0;
}