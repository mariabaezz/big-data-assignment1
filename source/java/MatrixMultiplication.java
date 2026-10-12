import java.util.Random;


public class MatrixMultiplication {

    public static void matrixMultiply(int[][] A, int[][] B, int[][] C) {

        int n = A.length;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {

                C[i][j] = 0;

                for (int k = 0; k < n; k++) {
                    C[i][j] += A[i][k] * B[k][j];
                }
            }
        }
    }


    public static int[][] generateMatrix(int n, Random random) {
        int[][] matrix = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = random.nextInt(10);
            }
        }

        return matrix;
    }
}