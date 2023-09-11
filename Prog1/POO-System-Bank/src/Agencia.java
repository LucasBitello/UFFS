import java.util.Scanner;

public class Agencia {
    private int id;
    public String name;

    public Agencia() {
        System.out.println("Defina o id da agencia: ");
        this.setIdByConsole();
        System.out.println("Defina o nome da agencia: ");
        this.setNameByConsole();
        this.printVariaveis();
    }

    public Agencia(int id, String name) {
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
        scanner.close();
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
        scanner.close();
    }

    public void printVariaveis() {
        System.out.println("######## valores da agencia ##########");
        System.out.println("id: " + this.id);
        System.out.println("Name: " + this.name);
    }
}
