#include "aed2_Servidor.h"

aed2_Servidor::aed2_Servidor() : _servidor(Servidor()){};

void aed2_Servidor::nuevaPartida(Jugador j, set<int> horizontales, set<int> verticales)
{
    _servidor.iniciarPartida(j, Mapa(horizontales, verticales));
}

void aed2_Servidor::agregarCasa(Jugador j, Casilla c)
{
    _servidor.agregarCasa(j, c);
}

void aed2_Servidor::agregarComercio(Jugador j, Casilla c)
{
    _servidor.agregarComercio(j, c);
}

void aed2_Servidor::avanzarTurno(Jugador j)
{
    _servidor.avanzarTurno(j);
}

void aed2_Servidor::unir(Jugador j1, Jugador j2) {
    _servidor.unir(j1,j2);
}

set<Casilla> aed2_Servidor::casas(Jugador j) {
    map<Casilla, Nat> casas = _servidor.partida(j).casas();
    set<Casilla> res;
    //Costo de adaptacion a la interfaz de la catedra. No se considera complejidad de copia
    for (const pair<const Casilla, Nat> casaAct : casas){
        res.insert(casaAct.first);
    }
    return res;
}

set<Casilla> aed2_Servidor::comercios(Jugador j)  {
    map<Casilla, Nat> comercios = _servidor.partida(j).comercios();
    set<Casilla> res;
    //Costo de adaptacion a la interfaz de la catedra. No se considera complejidad de copia
    for (const pair<const Casilla, Nat> comercioAct : comercios){
        res.insert(comercioAct.first);
    }
    return res;
}

Nat aed2_Servidor::nivel(Jugador j, Casilla c)  {
    return _servidor.nivel(j,c);
}

Nat aed2_Servidor::popularidad(Jugador j)  {
    return _servidor.popularidad(j);
}

Nat aed2_Servidor::antiguedad(Jugador j)  {
    return _servidor.turno(j);
}

bool aed2_Servidor::huboConstruccion(Jugador j)  {
    return _servidor.partida(j).agregoEnTurno();
}

set<int> aed2_Servidor::riosHorizontales(Jugador j)
{
    return _servidor.partida(j).mapa().horizontales();
}

set<int> aed2_Servidor::riosVerticales(Jugador j)  {
    return _servidor.partida(j).mapa().verticales();
}
