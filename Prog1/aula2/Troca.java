import java.util.Scanner;

public class Troca {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int vetDados[] = new int[20];

        for (int i = 0; i < vetDados.length; i++) {
            vetDados[i] = scanner.nextInt();
        }

        int vetDadosBkp[] = vetDados.clone();

        for (int i = 0; i <= 9; i++) {
            vetDados[i] = vetDadosBkp[vetDados.length - 1 - i];
            vetDados[vetDados.length - 1 - i] = vetDadosBkp[i];
        }

        for (int i = 0; i < vetDados.length; i++) System.out.printf("N[%d] = %d\n", i, vetDados[i]);
        scanner.close();
    }
}
