public class PruebaMoneda {
    public static void main(String[] args) {
        System.out.println(Moneda.values());
        for(Moneda moneda: Moneda.values()){
            System.out.println(moneda);
        }

        System.out.println(Moneda.Peso.ordinal());
    }
}
