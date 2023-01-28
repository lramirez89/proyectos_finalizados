import javax.swing.JOptionPane;

/**
 * La clase que es la entrada del programa
 * @author Leandro Ramirez
 * @version 0.1
 */
public class Principal{
    public static void main(String[] args) {
        Object[] lista = {"Conversor de moneda", "Conversor de temperatura (no implementado)"};
        JOptionPane.showInputDialog(null, "Seleccione una opción de conversión", "Conversor", 1, null, lista, null);
        System.out.println("fdsdf");
    }   
}