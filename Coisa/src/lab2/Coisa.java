
package lab2;


public class Coisa {
     public static void main(String[] args) {
         
        Aluno al = new Aluno("EDUARDO");
        al.cadastraCantina("mulherdobolo");
        al.cadastraLanche("mulherdobolo",5,4200);
        al.pagarConta("mulherdobolo", 420);
        System.out.println(al.cantinaToString("mulherdobolo"));
        
        

        
        
    }

   
}


   