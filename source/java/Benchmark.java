import java.util.Random;
import java.io.FileWriter;
import java.io.IOException;

public class Benchmark {

    public static void main(String[] args) throws IOException {

        int[] sizes = {50, 100, 150, 200, 250};
        int repetitions = 5;

        Random random = new Random(42);

        FileWriter writer = new FileWriter("../../results/java_results.csv");

        writer.write("language,matrix_size,repetition,execution_time_seconds\n");

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

                writer.write(
                    "Java," +
                    n + "," +
                    repetition + "," +
                    elapsedTime + "\n"
                );

                System.out.println(
                    "Size: " + n +
                    " | Repetition: " + repetition +
                    " | Time: " + elapsedTime + " seconds"
                );
            }
        }

        writer.close();
    }
}