public class App {
    public static void main(String[] args) throws Exception {
        Agencia agenciaA = new Agencia(1, "Nubank - 0001");
        Agencia agenciaB = new Agencia();

        Cliente clienteA = new Cliente(1, "Neymar Jr.");
        CartaoCredito cartaoCreditoClienteA = new CartaoCredito(001, "12/25");

        Cliente clienteB = new Cliente();
        CartaoCredito cartaoCreditoClienteB = new CartaoCredito();

        System.out.println("Cliente B solicitou alteração de nome: ");
        clienteB.setNameByConsole();
        clienteB.printVariaveis();
    }
}
