import java.util.Random;

public class Benchmark {

    public static void main(String[] args) {

        int[] sizes = {50, 100, 150, 200, 250};
        int repetitions = 5;

        Random random = new Random(42);

        for (int n : sizes) {

            int[][] A = MatrixMultiplication.generateMatrix(n, random);
            int[][] B = MatrixMultiplication.generateMatrix(n, random);

            // Warm-up
            MatrixMultiplication.matrixMultiply(A, B);

            for (int repetition = 1; repetition <= repetitions; repetition++) {

                long start = System.nanoTime();

                int[][] C = MatrixMultiplication.matrixMultiply(A, B);

                long end = System.nanoTime();

                double elapsedTime = (end - start) / 1_000_000_000.0;

                System.out.println(
                    "Size: " + n +
                    " | Repetition: " + repetition +
                    " | Time: " + elapsedTime + " seconds"
                );
            }
        }
    }
}