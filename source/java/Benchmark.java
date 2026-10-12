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


        FileWriter writer = new FileWriter("../../results/java_results.csv");

        writer.write("language,matrix_size,repetition,execution_time_seconds\n");

        for (int n : sizes) {

            int[][] A = readMatrix(
                "../../inputs/A_" + n + ".csv",
                n
            );

            int[][] B = readMatrix(
                "../../inputs/B_" + n + ".csv",
                n
            );

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