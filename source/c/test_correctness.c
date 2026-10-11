#include <stdio.h>

void matrix_multiply(int **A, int **B, int **C, int n);

int main() {

    // Test 1: Known matrices
    int A1_data[2][2] = {
        {1, 2},
        {3, 4}
    };

    int B1_data[2][2] = {
        {5, 6},
        {7, 8}
    };

    int C1_data[2][2] = {
        {0, 0},
        {0, 0}
    };

    int *A1[2] = {A1_data[0], A1_data[1]};
    int *B1[2] = {B1_data[0], B1_data[1]};
    int *C1[2] = {C1_data[0], C1_data[1]};

    matrix_multiply(A1, B1, C1, 2);

    if (
        C1[0][0] == 19 &&
        C1[0][1] == 22 &&
        C1[1][0] == 43 &&
        C1[1][1] == 50
    ) {
        printf("Known matrices test: true\n");
    } else {
        printf("Known matrices test: false\n");
    }


    // Test 2: Identity matrix
    int A2_data[3][3] = {
        {1, 0, 4},
        {3, 3, 2},
        {1, 8, 1}
    };

    int I_data[3][3] = {
        {1, 0, 0},
        {0, 1, 0},
        {0, 0, 1}
    };

    int C2_data[3][3] = {0};

    int *A2[3] = {A2_data[0], A2_data[1], A2_data[2]};
    int *I[3] = {I_data[0], I_data[1], I_data[2]};
    int *C2[3] = {C2_data[0], C2_data[1], C2_data[2]};

    matrix_multiply(A2, I, C2, 3);

    int identity_ok = 1;

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (C2[i][j] != A2[i][j]) {
                identity_ok = 0;
            }
        }
    }

    printf("Identity matrix test: %s\n", identity_ok ? "true" : "false");


    // Test 3: Zero matrix
    int Z_data[3][3] = {
        {0, 0, 0},
        {0, 0, 0},
        {0, 0, 0}
    };

    int C3_data[3][3] = {0};

    int *Z[3] = {Z_data[0], Z_data[1], Z_data[2]};
    int *C3[3] = {C3_data[0], C3_data[1], C3_data[2]};

    matrix_multiply(A2, Z, C3, 3);

    int zero_ok = 1;

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (C3[i][j] != 0) {
                zero_ok = 0;
            }
        }
    }

    printf("Zero matrix test: %s\n", zero_ok ? "true" : "false");

    return 0;
}