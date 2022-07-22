#include "SimCity.h"

SimCity::SimCity(const Mapa &m) : _mapa(m), _turno(0), _agregoEnTurno(false), _popularidad(0), _casas(), _comercios(){};

void SimCity::avanzarTurnoSC()
{
    sumar1Atodos(_casas);
    sumar1Atodos(_comercios);
    _turno++;
    _agregoEnTurno = false;
}

void SimCity::agregarCasaSC(Casilla p)
{
    _casas.insert(make_pair(p, 0));
    _agregoEnTurno = true;
}

void SimCity::agregarComercioSC(Casilla p)
{
    _comercios.insert(make_pair(p, 0));
    _agregoEnTurno = true;
}

void SimCity::unirParametros(SimCity &s)
{
    if (_turno < s.turnoSC())
    {
        _turno = s.turnoSC();
    }

    _popularidad += 1;
    _popularidad += s.popularidadSC();
    _agregoEnTurno = _agregoEnTurno or s.agregoEnTurno();
}

void SimCity::unirMapaYconstrucciones(SimCity &s, Nat turnosACompensar)
{
    unirMapas(s);
    unirCasas(s, turnosACompensar);
    unirComercios(s, turnosACompensar);
    actualizarComercios();
}

void SimCity::unirMapas(SimCity &s)
{
    set<int> horS1 = mapa().horizontales();
    set<int> horS2 = s.mapa().horizontales();
    for (int itHorS2 : horS2)
    {
        horS1.insert(itHorS2);
    }

    set<int> verS1 = mapa().verticales();
    set<int> verS2 = s.mapa().verticales();
    for (int itVerS2 : verS2)
    {
        verS1.insert(itVerS2);
    }

    _mapa = Mapa(horS1, verS1);
}

void SimCity::unirCasas(SimCity &s, Nat turnosACompensar)
{
    map<Casilla, Nat> casasS2 = s.casas();
    for (const pair<const Casilla, Nat> &casaS2Act : casasS2)
    {
        if (_casas.count(casaS2Act.first) == 0 or (_casas.count(casaS2Act.first) == 1 && casaS2Act.second > _casas.at(casaS2Act.first)))
        {
            _casas[casaS2Act.first] = casaS2Act.second;
            if (turnosACompensar > 0)
            {
                _casas[casaS2Act.first] += turnosACompensar;
            }
            if (_comercios.count(casaS2Act.first) == 1)
            {
                _comercios.erase(casaS2Act.first);
            }
        }
    }
}

void SimCity::unirComercios(SimCity &s, Nat turnosACompensar)
{
    map<Casilla, Nat> comS2 = s.comercios();
    for (const pair<const Casilla, Nat> &comS2Act : comS2)
    {
        if ((_casas.count(comS2Act.first) == 0) &&
            ((_comercios.count(comS2Act.first) == 0 or (_comercios.count(comS2Act.first) == 1 && comS2Act.second > _comercios.at(comS2Act.first)))))
        {
            _comercios[comS2Act.first] = comS2Act.second;
            if (turnosACompensar > 0)
            {
                _comercios[comS2Act.first] += turnosACompensar;
            }
        }
    }
}

void SimCity::actualizarComercios()
{
    for (pair<const Casilla, Nat> &comercioAct : _comercios)
    {

        for (const pair<const Casilla, Nat> casaAct : _casas)
        {
            if (distanciaDeManhattan(comercioAct.first, casaAct.first) <= 3 &&
                casaAct.second > comercioAct.second)
            {
                comercioAct.second = casaAct.second;
            }
        }
    }
}

void SimCity::sumar1Atodos(map<Casilla, Nat> &m)
{
    for (pair<const Casilla, Nat> &entradaDicc : m)
    {
        entradaDicc.second++;
    }
}

Nat SimCity::distanciaDeManhattan(const Casilla &p1, const Casilla &p2)
{
    return abs(p1.first - p2.first) + abs(p1.second - p2.second);
}

map<Casilla, Nat> SimCity::casas() const
{
    return _casas;
}

map<Casilla, Nat> SimCity::comercios()
{
    actualizarComercios();
    return _comercios;
}

Mapa SimCity::mapa() const
{
    return _mapa;
}

Nat SimCity::turnoSC() const
{
    return _turno;
}

Nat SimCity::popularidadSC() const
{
    return _popularidad;
}

bool SimCity::agregoEnTurno() const
{
    return _agregoEnTurno;
}