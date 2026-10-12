import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class MemoryTest {

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

        int n = Integer.parseInt(args[0]);

        int[][] A = readMatrix(
            "../../inputs/A_" + n + ".csv",
            n
        );

        int[][] B = readMatrix(
            "../../inputs/B_" + n + ".csv",
            n
        );

        int[][] C = MatrixMultiplication.matrixMultiply(A, B);
    }
}