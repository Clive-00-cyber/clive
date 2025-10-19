import javax.swing.JOptionPane;

public class test{
    public static void main(String args[]){
        String cha1, cha2;
        int ent1, ent2, sum;
        cha1=JOptionPane.showInputDialog("Enter a number");
        cha2=JOptionPane.showInputDialog("Enter a number");
        ent1=Integer.parseInt(cha1);
        ent2=Integer.parseInt(cha2);
        sum=ent1+ent2;
        JOptionPane.showMessageDialog(null,"Sum ="+sum);
    }
}