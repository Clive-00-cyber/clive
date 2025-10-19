public class Rectangle {
    public int largeur;
    public int hauteur;
    public String nom;

    public Rectangle(int largeur, int hauteur,String nom) {
        this.largeur = largeur;
        this.hauteur = hauteur;
        this.nom = nom;
    }

    public void afficher() {
        System.out.println("Rectangle " +nom+ " de largeur " + largeur + " hauteur " + hauteur);
    }

    public int per() {
        return 2 * (largeur + hauteur);
    }

    public int surf() {
        return largeur * hauteur;
    }

    public void compare(Rectangle r1, Rectangle r2){
        if (r1.largeur == r2.largeur && r1.hauteur == r2.hauteur) {
            System.out.println("Les deux rectangles ont les mêmes dimensions.");
        } else if (r1.largeur > r2.largeur && r1.hauteur > r2.hauteur) {
            System.out.println("Rectangle "+r1.nom+" est plus grand en largeur et hauteur.");
        } else if (r1.largeur < r2.largeur && r1.hauteur < r2.hauteur) {
            System.out.println("Rectangle "+r2.nom+" est plus grand en largeur et hauteur.");
        } else {
            System.out.println("Les rectangles ont des dimensions différentes sans être strictement plus grands.");
        }
    }
}
