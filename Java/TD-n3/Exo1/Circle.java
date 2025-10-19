public class Circle extends Shape {
    @SuppressWarnings("unused")
    final static double P = 3.14;
    private double radius;
    private double surface=0;

    public Circle() {
        radius = 0;
    }
    public Circle(double x, double y, double r){
        super(x,y);
        radius=r;
    }
    @SuppressWarnings("override")
    public String toString(){
        return super.toString()+"Raduis= "+radius+"Surface= "+surface;
    }
    public void getRadius(double R){
        this.radius=R;
    }
    public String setRadius(){
        return "Radius= "+radius+"Surface= "+surface;
    }
    public double setSurface(){
        return surface;
    }
    public void getSurface(double S){
        this.surface=S;
    }
    public int isBigger(Circle c1,Circle c2){
        if(c1.surface>c2.surface){
            return 1;
        }else return 0;
    }  
}
