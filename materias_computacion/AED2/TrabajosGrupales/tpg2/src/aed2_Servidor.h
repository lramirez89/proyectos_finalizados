#ifndef AED2_SERVIDOR_H
#define AED2_SERVIDOR_H

#include "Tipos.h"
#include "Servidor.h"

class aed2_Servidor
{
public:
    aed2_Servidor();

    void nuevaPartida(Jugador j, set<int> horizontales, set<int> verticales);

    void agregarCasa(Jugador j, Casilla c);

    void agregarComercio(Jugador j, Casilla c);

    void avanzarTurno(Jugador j);

    void unir(Jugador j1, Jugador j2);

    set<int> riosHorizontales(Jugador j);

    set<int> riosVerticales(Jugador j);

    set<Casilla> casas(Jugador j);

    set<Casilla> comercios(Jugador j);

    Nat nivel(Jugador j, Casilla c);

    bool huboConstruccion(Jugador j);

    Nat popularidad(Jugador j) ;

    Nat antiguedad(Jugador j) ;

private:
    Servidor _servidor;
};

#endif // AED2_SERVIDOR_H