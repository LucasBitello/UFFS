import java.util.Scanner;

public class Diagonal {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String tipoOperacao = scanner.nextLine().toUpperCase();
        float matrizDados[][] = new float[12][12];
        float sumDiagSuperior = 0;
        float numItensDiagSuperior = 0;

        for (int i = 0; i < matrizDados.length; i++) {
            for (int j = 0; j < matrizDados.length; j++) {
                matrizDados[i][j] = scanner.nextFloat();

                if (i < j) {
                    sumDiagSuperior += matrizDados[i][j];
                    numItensDiagSuperior++;
                }
            }
        }

        if (tipoOperacao.equals("S")) {
            System.out.printf("%.1f\n", sumDiagSuperior);
        } else if (tipoOperacao.equals("M")) {
            System.out.printf("%.1f\n", sumDiagSuperior / numItensDiagSuperior);
        }

        scanner.close();
    }
}
