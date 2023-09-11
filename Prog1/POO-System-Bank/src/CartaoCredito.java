import java.util.Scanner;

public class CartaoCredito {
    private int numeroCartao;
    private String dataValidade;

    public CartaoCredito() {
        System.out.println("Defina o numero do cartão: ");
        this.setNumeroCartaoByConsole();
        System.out.println("Defina a data de validade: ");
        this.setDataValidadeByConsole();
        this.printVariaveis();
    }

    public CartaoCredito(int numero_cartao, String data_validade) {
        this.numeroCartao = numero_cartao;
        this.dataValidade = data_validade;
        this.printVariaveis();
    }

    public int getNumeroCartao() {
        return this.numeroCartao;
    }

    public void setNumeroCartao(int numeroCartao) {
        this.numeroCartao = numeroCartao;
    }

    public void setNumeroCartaoByConsole() {
        Scanner scanner = new Scanner(System.in);
        this.numeroCartao = scanner.nextInt();
        scanner.close();
    }

    public String getDataValidade() {
        return this.dataValidade;
    }

    public void setDataValidade(String dataValidade) {
        this.dataValidade = dataValidade;
    }

    public void setDataValidadeByConsole() {
        Scanner scanner = new Scanner(System.in);
        this.dataValidade = scanner.nextLine();
        scanner.close();
    }

    public void printVariaveis() {
        System.out.println("######## valores do cartão de crédito ##########");
        System.out.println("Numero Cartão: " + this.numeroCartao);
        System.out.println("Data Validade: " + this.dataValidade);
    }
}