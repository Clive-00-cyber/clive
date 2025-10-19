import java.util.Scanner;

public class Main {
    @SuppressWarnings("ConvertToTryWithResources")
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Entre le nom du premier rectangle");
        String nom1 = input.next();

        System.out.print("Entrez la largeur du premier rectangle: ");
        int largeur1 = input.nextInt();

        System.out.print("Entrez la longueur du premier rectangle: ");
        int hauteur1 = input.nextInt();

        System.out.println("Entre le nom du second rectangle");
        String nom2 = input.next();

        System.out.print("Entrez la largeur du second rectangle: ");
        int largeur2 = input.nextInt();

        System.out.print("Entrez la longueur du second rectangle: ");
        int hauteur2 = input.nextInt();
        

        Rectangle rec = new Rectangle(largeur1, hauteur1, nom1);
        Rectangle r6 = new Rectangle(largeur2, hauteur2, nom2);

        rec.afficher();
        System.out.println("Périmètre: " + rec.per() + " Aire: " + rec.surf());
        r6.afficher();
        System.out.println("Périmètre: " + r6.per() + " Aire: " + r6.surf());  

        rec.compare(rec,r6);

        input.close();
    }
}

