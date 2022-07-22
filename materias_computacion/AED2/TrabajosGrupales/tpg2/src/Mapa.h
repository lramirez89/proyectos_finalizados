#ifndef MAPA
#define MAPA

#include "Tipos.h"

class Mapa
{
public:
    Mapa(set<int> &hs, set<int> &vs);

    set<int> horizontales();

    set<int> verticales();

private:
    set<int> _hs;
    set<int> _vs;
};

#endif