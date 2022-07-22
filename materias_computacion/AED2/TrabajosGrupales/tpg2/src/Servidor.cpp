#include "Servidor.h"

Servidor::Servidor() : trie(){};

Servidor::valorTrie::valorTrie(const Mapa &m) : simCity(SimCity(m)), fueUnion(false), uniones(list<Jugador>()), turnosAcomp(0) {}

void Servidor::iniciarPartida(const Jugador &j, const Mapa &m)
{
    trie.insert(make_pair(j, Servidor::valorTrie(m)));
}

void Servidor::agregarCasa(const Jugador &j, Casilla p)
{
    (trie.at(j)).simCity.agregarCasaSC(p);
}

void Servidor::agregarComercio(const Jugador &j, Casilla p)
{
    (trie.at(j)).simCity.agregarComercioSC(p);
}

void Servidor::avanzarTurno(const Jugador &j)
{
    Servidor::valorTrie &data = trie.at(j);
    data.simCity.avanzarTurnoSC();
    if (!data.uniones.empty())
    { // O(1)
        data.turnosAcomp++;
    }
}

void Servidor::unir(const Jugador &j1, const Jugador &j2)
{
    Servidor::valorTrie &dataJ1 = trie.at(j1);
    Servidor::valorTrie &dataJ2 = trie.at(j2);

    dataJ1.simCity.unirParametros(dataJ2.simCity); // O(1)

    dataJ1.uniones.push_back(j2); // Agregamos J2 a la lista de uniones de J1
    dataJ2.fueUnion = true;       // Marcamos que fue union

    return;
}

void Servidor::actualizarPartida(const Jugador &j)
{
    Servidor::valorTrie &dataJ = trie.at(j);
    SimCity &partida = dataJ.simCity;
    list<Jugador> &uniones = dataJ.uniones;
    Nat &turnosAcompensar = dataJ.turnosAcomp;
    for (Jugador actUnion : uniones)
    {
        // Si lo que vamos a unir quedo con actualizaciones pendientes, primero resolvemos eso
        Servidor::valorTrie &dataUnionAct = trie.at(actUnion);
        if (dataUnionAct.uniones.size() > 0)
        {
            actualizarPartida(actUnion);
        };

        partida.unirMapaYconstrucciones(dataUnionAct.simCity, turnosAcompensar);
        if (turnosAcompensar > 0)
        {
            turnosAcompensar--;
        }
    }

    return;
}

Nat Servidor::popularidad(const Jugador &j)
{
    return trie.at(j).simCity.popularidadSC();
}

SimCity Servidor::partida(const Jugador &j)
{
    actualizarPartida(j);
    return trie.at(j).simCity;
}

Nat Servidor::turno(const Jugador &j)
{
    return trie.at(j).simCity.turnoSC();
}

Nat Servidor::nivel(const Jugador &j, Casilla c)
{
    SimCity partida = trie.at(j).simCity;
    if (partida.comercios().count(c) == 1)
    {
        return partida.comercios().at(c);
    }
    else
    {
        return partida.casas().at(c);
    }
}

bool Servidor::fueUnion(const Jugador &j)
{
    return trie.at(j).fueUnion;
}