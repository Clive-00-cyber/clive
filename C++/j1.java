public class rational{
    public:
    int a;
    int b;
    public rational(int a,int b){
        this.a=a;
        this.b=b;
    }
    public string printRational(){
        return(a"/"b);
    }
    public static void main(string[] args){
        rational r1=new rational(2,3);
        r1.printRational();
    }

}