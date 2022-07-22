#include "Mapa.h"

Mapa::Mapa(set<int> &hs, set<int> &vs) : _hs(hs), _vs(vs){};

set<int> Mapa::horizontales()
{
    return _hs;
};

set<int> Mapa::verticales()
{
    return _vs;
}