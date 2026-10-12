import java.io.FileWriter;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.FileReader;

public class Benchmark {

    public static int[][] readMatrix(String filename, int n) throws IOException {

        int[][] matrix = new int[n][n];

        BufferedReader reader = new BufferedReader(new FileReader(filename));

        String line;
        int row = 0;

        while ((line = reader.readLine()) != null) {

            String[] values = line.split(",");

            for (int col = 0; col < n; col++) {
                matrix[row][col] = Integer.parseInt(values[col]);
            }

            row++;
        }

        reader.close();

        return matrix;
    }


    public static void main(String[] args) throws IOException {

        int[] sizes = {50, 100, 150, 200, 250};
        int repetitions = 5;

        FileWriter writer =
            new FileWriter("../../results/java_results.csv");

        writer.write(
            "language,matrix_size,repetition,execution_time_seconds,checksum\n"
        );

        for (int n : sizes) {

            int[][] A = readMatrix(
                "../../inputs/A_" + n + ".csv",
                n
            );

            int[][] B = readMatrix(
                "../../inputs/B_" + n + ".csv",
                n
            );

            int[][] C = new int[n][n];

            // Warm-up: 3 executions
            for (int warmup = 0; warmup < 3; warmup++) {
                MatrixMultiplication.matrixMultiply(A, B, C);
            }

            for (int repetition = 1; repetition <= repetitions; repetition++) {

                long start = System.nanoTime();

                MatrixMultiplication.matrixMultiply(A, B, C);

                long end = System.nanoTime();

                double elapsedTime =
                    (end - start) / 1_000_000_000.0;
                
                long checksum = 0;

                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < n; j++) {
                        checksum += C[i][j];
                    }
                }

                writer.write(
                    "Java," +
                    n + "," +
                    repetition + "," +
                    elapsedTime + "," +
                    checksum + "\n"
                );

                System.out.println(
                    "Size: " + n +
                    " | Repetition: " + repetition +
                    " | Time: " + elapsedTime + " seconds" +
                    " | Checksum: " + checksum
                );
            }
        }

        writer.close();
    }
}