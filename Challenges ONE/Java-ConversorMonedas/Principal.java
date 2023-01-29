import javax.swing.JOptionPane;

/**
 * La clase que es la entrada del programa
 * @author Leandro Ramirez
 * @version 0.1
 */
public class Principal{
    public static void main(String[] args) {
        //primer menú. Se debe elegir conversor de moneda
        int deseaContinuar= 0;
        while(deseaContinuar==0){
            Object[] lista = {"Conversor de moneda", "Conversor de temperatura (no implementado)"};
            Object opcion = JOptionPane.showInputDialog(null, "Seleccione una opción de conversión", "Conversor", 1, null, lista, null);
    
            if(opcion.toString() == lista[0]){
                //elegir moneda a vender
                Moneda monAVender = (Moneda) JOptionPane.showInputDialog(null, "Seleccione una moneda", "Conversor de monedas", 1, null, Moneda.values(), null);
    
                //mostramos opciones para convertir de monAVender
                Moneda monAComprar = (Moneda) JOptionPane.showInputDialog(null, "Seleccione una moneda", "Convirtiendo de " + monAVender + " a:", 1, null, Moneda.values(), null);
                try{
                    Double cantidad =  Double.valueOf(JOptionPane.showInputDialog("Ingrese la cantidad de dinero que deseas convertir:")) ;

                    Double cantComprada = monAVender.vender( cantidad, monAComprar);
                    String mensaje = "Tienes $ " + cantComprada + " "+ monAComprar +"s";
                    JOptionPane.showMessageDialog(null, mensaje, "Mensaje", 0, null);
    
                    //muestro dialogo de confirmación
                    deseaContinuar  = JOptionPane.showConfirmDialog(null, "Desea continuar?");

                    if(deseaContinuar >= 1)
                        JOptionPane.showMessageDialog(null, "Programa terminado", "Mensaje", 0, null);
                }catch(NumberFormatException ex){
                    JOptionPane.showMessageDialog(null, "Debe ingresar un número decimal. Use , en lugar de .", "Mensaje", 0, null);                    
                }   
        
            }else{
                JOptionPane.showMessageDialog(null, "Conversor todavía no implementado", "Mensaje", 0, null);
            }
        }
    } 
}