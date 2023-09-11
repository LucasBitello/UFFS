public class App {
    public static void main(String[] args) throws Exception {
        Conta c1 = new Conta(1);
        
        System.out.println("Numero C1: " + c1.getNumero());
        System.out.println("Saldo C1: " + c1.getSaldo());
        System.out.println("Limite C1: " + c1.getLimite());

        Conta c2 = new Conta(2, 5000, 2000);
        
        System.out.println("Numero C2: " + c2.getNumero());
        System.out.println("Saldo C2: " + c2.getSaldo());
        System.out.println("Limite C2: " + c2.getLimite());
    }
}
