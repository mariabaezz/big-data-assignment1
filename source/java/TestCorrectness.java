import java.util.Arrays;

public class TestCorrectness {

    public static void main(String[] args) {

        // Test 1: Known matrices
        int[][] A = {
            {1, 2},
            {3, 4}
        };

        int[][] B = {
            {5, 6},
            {7, 8}
        };

        int[][] expected = {
            {19, 22},
            {43, 50}
        };

        int[][] result = new int[2][2];

        MatrixMultiplication.matrixMultiply(A, B, result);

        System.out.println(
            "Known matrices test: " +
            Arrays.deepEquals(result, expected)
        );


        // Test 2: Identity matrix
        int[][] A2 = {
            {1, 0, 4},
            {3, 3, 2},
            {1, 8, 1}
        };

        int[][] I = {
            {1, 0, 0},
            {0, 1, 0},
            {0, 0, 1}
        };

        result = new int[3][3];

        MatrixMultiplication.matrixMultiply(A2, I, result);

        System.out.println(
            "Identity matrix test: " +
            Arrays.deepEquals(result, A2)
        );


        // Test 3: Zero matrix
        int[][] Z = {
            {0, 0, 0},
            {0, 0, 0},
            {0, 0, 0}
        };

        int[][] expectedZero = {
            {0, 0, 0},
            {0, 0, 0},
            {0, 0, 0}
        };

        result = new int[3][3];

        MatrixMultiplication.matrixMultiply(A2, Z, result);

        System.out.println(
            "Zero matrix test: " +
            Arrays.deepEquals(result, expectedZero)
        );
    }
}