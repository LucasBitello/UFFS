import java.util.Scanner;

public class Cliente {
    private int id;
    public String name;

    public Cliente() {
        System.out.println("####### Novo cliente #######");
        System.out.println("Defina o id do cliente: ");
        this.setIdByConsole();
        System.out.println("Defina o nome do cliente: ");
        this.setNameByConsole();
        this.printVariaveis();
    }

    public Cliente(int id, String name) {
        this.id = id;
        this.name = name;
        this.printVariaveis();
    }

    public int getId() {
        return this.id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setIdByConsole() {
        Scanner scanner = new Scanner(System.in);
        this.id = scanner.nextInt();
    }

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setNameByConsole() {
        Scanner scanner = new Scanner(System.in);
        this.name = scanner.nextLine();
    }

    public void printVariaveis() {
        System.out.println("######## valores do usuário ##########");
        System.out.println("id: " + this.id);
        System.out.println("Name: " + this.name);
        System.out.println("");
    }
}
