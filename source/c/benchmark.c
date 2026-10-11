#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void matrix_multiply(int **A, int **B, int **C, int n);
int **generate_matrix(int n);
int **create_empty_matrix(int n);
void free_matrix(int **matrix, int n);


int main() {

    int sizes[] = {50, 100, 150, 200, 250};
    int repetitions = 5;

    srand(42);

    FILE *file = fopen("../../results/c_results.csv", "w");

    fprintf(file, "language,matrix_size,repetition,execution_time_seconds\n");

    for (int s = 0; s < 5; s++) {

        int n = sizes[s];

        int **A = generate_matrix(n);
        int **B = generate_matrix(n);
        int **C = create_empty_matrix(n);

        for (int repetition = 1; repetition <= repetitions; repetition++) {

            clock_t start = clock();

            matrix_multiply(A, B, C, n);

            clock_t end = clock();

            double elapsed_time =
                (double)(end - start) / CLOCKS_PER_SEC;

            printf(
                "Size: %d | Repetition: %d | Time: %f seconds\n",
                n,
                repetition,
                elapsed_time
            );

            fprintf(
                file,
                "C,%d,%d,%f\n",
                n,
                repetition,
                elapsed_time
            );
        }

        free_matrix(A, n);
        free_matrix(B, n);
        free_matrix(C, n);
    }

    fclose(file);

    return 0;
}