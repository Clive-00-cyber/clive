public class Cylindre extends Circle{
        private double h;
    public Cylindre(){
        h=0;
    }
    public Cylindre(double height){
        h=height;
    }
    public double setheight(){
        return h;
    }
    public void getheight(double H){
        this.h=H;
    }
    @SuppressWarnings("static-access")
    public double aire(){
        return 2*super.setSurface()+2*super.P*h;
    }
    public double volume(){
        return super.setSurface()*h;
    }
        @Override
    public String toString(){
        return super.toString()+"height= "+h;
    }
}
