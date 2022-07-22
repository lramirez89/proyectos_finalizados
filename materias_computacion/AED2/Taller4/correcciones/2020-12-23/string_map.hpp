
#include "string_map.h"

template <typename T>
string_map<T>::string_map() : _size(0), raiz(nullptr){}

template <typename T>
string_map<T>::string_map(const string_map<T>& aCopiar) : string_map() { *this = aCopiar; } // Provisto por la catedra: utiliza el operador asignacion para realizar la copia.

template <typename T>
string_map<T>& string_map<T>::operator=(const string_map<T>& d) {
    if(raiz != nullptr) raiz->destruir();

    if(d.raiz != nullptr){
        raiz = new Nodo();
        if(d.raiz->definicion) raiz->definicion = new T(*(d.raiz->definicion));
        raiz->copiar(d.raiz->siguientes);
    } else {
        raiz = nullptr;
    }

    return *this;
}

template <typename T>
string_map<T>::~string_map(){
    if(raiz != nullptr) raiz->destruir();
}

template <typename T>
T& string_map<T>::operator[](const string& clave){
    //COMPLETAR
    //return nullptr;
}


template<typename T>
void string_map<T>::insert(const pair<string, T> & par) {

    if(raiz == nullptr){
        raiz = new Nodo();
    }

    Nodo* actual = raiz;
    for(int i = 0; i<par.first.size(); i++){
        int letra = int(par.first[i]);
        if(actual->siguientes[letra] == nullptr) {
            actual->siguientes[letra] = new Nodo();
            actual->child_count++;
        }
        actual = actual->siguientes[letra];
    }

    if(actual->definicion != nullptr) delete actual->definicion;

    actual->definicion = new T(par.second);

    _size++;
}

template <typename T>
int string_map<T>::count(const string& clave) const{
    if(raiz == nullptr){
        return 0;
    }

    Nodo* actual = raiz;
    for(int i = 0; i<clave.size(); i++){
        int letra = int(clave[i]);
        if(actual->siguientes[letra] == nullptr) {
            return 0;
        }
        actual = actual->siguientes[letra];
    }
    if(actual->definicion != nullptr) return 1;

    return 0;
}

template <typename T>
const T& string_map<T>::at(const string& clave) const {

    Nodo* actual = raiz;
    for(int i = 0; i<clave.size(); i++){
        int letra = int(clave[i]);
        actual = actual->siguientes[letra];
    }

    return actual->definicion;
}

template <typename T>
T& string_map<T>::at(const string& clave) {
    Nodo* actual = raiz;
    for(int i = 0; i<clave.size(); i++){
        int letra = int(clave[i]);
        actual = actual->siguientes[letra];
    }

    return *(actual->definicion);
}

template <typename T>
void string_map<T>::erase(const string& clave) {

    if(clave != ""){
        Nodo *actual = raiz;
        Nodo *ultimo_nodo = raiz;
        int pos = 0;

        for (int i = 0; i < clave.size(); i++) {
            int letra = int(clave[i]);
            actual = actual->siguientes[letra];
            if (actual->child_count > 1 || actual->definicion != nullptr) {
                ultimo_nodo = actual;
                pos = i;
            }
        }

        if(actual->definicion) delete actual->definicion;
        actual->definicion = nullptr;

        if (actual->child_count == 0) {
            int letra = int(clave[pos]);
            Nodo *siguiente = ultimo_nodo->siguientes[letra];
            ultimo_nodo->child_count--;
            ultimo_nodo = siguiente;
            pos++;
            while (pos < clave.size()) {
                int letra = int(clave[pos]);
                Nodo *siguiente = ultimo_nodo->siguientes[letra];
                delete ultimo_nodo;
                ultimo_nodo = siguiente;
                pos++;
            }
        }
    } else {
        if(raiz->definicion) delete raiz->definicion;
        raiz->definicion = nullptr;
        if(raiz->child_count == 0){
            delete raiz;
            raiz = nullptr;
        }
    }
    _size--;
}

template <typename T>
int string_map<T>::size() const{
    return _size;
}

template <typename T>
bool string_map<T>::empty() const{
    return raiz == nullptr;
}

template<typename T>
void string_map<T>::Nodo::destruir() {
    if(child_count != 0){
       for(int i = 0; i < 256; i++){
           if(siguientes[i] != nullptr){
               siguientes[i]->destruir();
           }
       }
    }
    if(definicion) delete definicion;
    delete this;
}

template<typename T>
void string_map<T>::Nodo::copiar(const vector<Nodo*>& aCopiar) {
    for(int i = 0; i < 256; i++){
        if(aCopiar[i] != nullptr){
            siguientes[i] = new Nodo();
            if(aCopiar[i]->definicion) siguientes[i]->definicion = new T(*(aCopiar[i]->definicion));
            siguientes[i]->copiar(aCopiar[i]->siguientes);
            child_count++;
        }
    }
}
