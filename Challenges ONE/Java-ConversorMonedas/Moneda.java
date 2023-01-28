/**
 * Implentación de las monedas a convertir
 */
public enum Moneda {
    Peso, Dolar, Euro, Libra, Yen, Won_Coreano;

    @Override
    public String toString() {
        if(this.name() == Moneda.Peso.name())
            return "Peso";
        if(this.name() == Moneda.Dolar.name())
            return "Dolar";
        if(this.name() == Moneda.Euro.name())
            return "Euro";    
        if(this.name() == Moneda.Libra.name())
            return "Libra";
        if(this.name() == Moneda.Yen.name())
            return "Yen";
        if(this.name() == Moneda.Won_Coreano.name())
            return "Won Coreano";
        else{
            return "";
        }
    }

    /**
     * Devuelve la cotización para la venta de mon1 para comprar mon2
     * @param mon1 
     * @param mon2
     * @return
     */
    private static double cotizacionVenta(Moneda mon1, Moneda mon2){
        if(mon1 == Peso && mon2 == Peso)
            return 0;
        if(mon1 == Peso && mon2 == Dolar)
            return 0.3;
        if(mon1 == Peso && mon2 == Euro)
            return 0.4;
        if(mon1 == Peso && mon2 == Libra)
            return 0.5;
        if(mon1 == Peso && mon2 == Yen)
            return 0.6;
        if(mon1 == Peso && mon2 == Won_Coreano)
            return 0.4;
        if(mon1 == Dolar && mon2 == Peso)
            return 286;
        else
            return 0;
    }

    /**
     * Devuelve la cantidad en la moneda mon que se obtiene de vender cantidad instanciada 
     * @param cantidad
     * @param mon
     */
    public double vender(double cantidad, Moneda mon){
        return Moneda.cotizacionVenta(this, mon)*cantidad;
    }
}
