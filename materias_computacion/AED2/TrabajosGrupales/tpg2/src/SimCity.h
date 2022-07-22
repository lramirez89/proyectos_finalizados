#ifndef SC
#define SC

#include "Tipos.h"
#include "Mapa.h"

class SimCity
{
public:
    explicit SimCity(const Mapa &m);

    void avanzarTurnoSC();

    void agregarCasaSC(Casilla p);

    void agregarComercioSC(Casilla p);

    void unirParametros(SimCity &s); // O(1)

    void unirMapaYconstrucciones(SimCity &s, Nat turnosAcompensar);

    Mapa mapa() const;

    map<Casilla, Nat> casas() const;

    map<Casilla, Nat> comercios();

    Nat popularidadSC() const;

    Nat turnoSC() const;

    bool agregoEnTurno() const;

private:
    Mapa _mapa;
    Nat _turno;
    bool _agregoEnTurno;
    Nat _popularidad;
    map<Casilla, Nat> _casas;
    map<Casilla, Nat> _comercios;

    void actualizarComercios();

    void unirMapas(SimCity &s);

    void unirCasas(SimCity &s, Nat turnosAcompensar);

    void unirComercios(SimCity &s, Nat turnosAcompensar);

    static void sumar1Atodos(map<Casilla, Nat> &m);

    static Nat distanciaDeManhattan(const Casilla &p1, const Casilla &p2);
};

#endif // SC