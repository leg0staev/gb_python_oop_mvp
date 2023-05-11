package java;

public class Program {
    public static void main(String[] args) {
        
        var m = new SumModel();
        var v = new View();

        Presenter p = new Presenter(m, v);

        p.buttonClick();


    }
}
