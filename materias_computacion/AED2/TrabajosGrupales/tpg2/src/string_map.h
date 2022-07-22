#ifndef STRING_MAP_H_
#define STRING_MAP_H_

#include <string>
#include <vector>

using namespace std;

template <typename T>
class string_map
{
public:

    string_map();

    ~string_map();

    string_map(const string_map<T> &aCopiar);

    string_map &operator=(const string_map &d);

    void insert(const pair<string, T> &);

    int count(const string &key) const;

    const T &at(const string &key) const;

    T &at(const string &key);

    void erase(const string &key);

    int size() const;

    bool empty() const;

    T &operator[](const string &key);

private:
    struct Nodo
    {
        vector<Nodo *> siguientes;
        T *definicion;

        Nodo();

        Nodo(T *def);
    };

    Nodo *raiz;
    int _size;

    Nodo *search(const string &clave) const;

    void deleteWithChildren(Nodo* actual);

    void copyChildren(Nodo *actCopia, Nodo* actD);

    bool deleteNonRelevantNodes(Nodo* actual, vector<char> &vecClave, int i);

    bool irrelevantNode(Nodo* actual);
};

#include "string_map.hpp"

#endif // STRING_MAP_H_
