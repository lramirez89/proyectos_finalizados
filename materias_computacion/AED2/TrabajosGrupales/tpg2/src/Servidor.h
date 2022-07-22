#ifndef SERVIDOR_H
#define SERVIDOR_H

#include "string_map.h"
#include "SimCity.h"
#include "Mapa.h"
#include "Tipos.h"

class Servidor
{
public:
    Servidor();

    void iniciarPartida(const Jugador &j, const Mapa &m);

    void agregarCasa(const Jugador &j, Casilla p);

    void agregarComercio(const Jugador &j, Casilla p);

    void avanzarTurno(const Jugador &j);

    void actualizarPartida(const Jugador &j);

    void unir(const Jugador &j1, const Jugador &j2);

    Nat popularidad(const Jugador &j);

    SimCity partida(const Jugador &j);

    Nat turno(const Jugador &j);

    Nat nivel(const Jugador &j, Casilla c);

    bool fueUnion(const Jugador &j);

private:
    // El 4° parametro es turnos a compensar (#veces que se llamo a avanzarTurno luego de una/s union/es sin llamar a un observador)
    struct valorTrie
    {
        SimCity simCity;
        bool fueUnion;
        list<Jugador> uniones;
        Nat turnosAcomp;

        explicit valorTrie(const Mapa &m);
    };

    string_map<valorTrie> trie;
};

#endif // SERVIDOR_H