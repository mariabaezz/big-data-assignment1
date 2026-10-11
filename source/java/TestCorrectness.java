import java.util.Arrays;

public class TestCorrectness {

    public static void main(String[] args) {

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

        int[][] result = MatrixMultiplication.matrixMultiply(A, B);

        System.out.println(
            "Known matrices test: " +
            Arrays.deepEquals(result, expected)
        );


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

        result = MatrixMultiplication.matrixMultiply(A2, I);

        System.out.println(
            "Identity matrix test: " +
            Arrays.deepEquals(result, A2)
        );


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

        result = MatrixMultiplication.matrixMultiply(A2, Z);

        System.out.println(
            "Zero matrix test: " +
            Arrays.deepEquals(result, expectedZero)
        );
    }
}