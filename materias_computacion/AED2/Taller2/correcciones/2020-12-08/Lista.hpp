#include "Lista.h"

Lista::Lista(): _primero(nullptr), _longitud(0){
}

Lista::Lista(const Lista& l) : Lista() {
    //Inicializa una lista vacía y luego utiliza operator= para no duplicar el código de la copia de una lista.
    *this = l;
}

Lista::~Lista() {
    // Completar
    //Destructor de la lista vacia
    int temp= this->_longitud;
    for (int i = 0; i< temp ; i++){
        (*this).eliminar(0);
    }
}

Lista& Lista::operator=(const Lista& aCopiar) {
    // Completar
    (*this).~Lista();
    for(int i=0; i<aCopiar.longitud() ;i++){
        agregarAtras(aCopiar.iesimo(i));
    }
    return *this;
}

void Lista::agregarAdelante(const int& elem) {
    // Completar
    if(_primero==nullptr){
        Nodo* nuevo= new Nodo;
        (*nuevo)={elem, nuevo, nuevo};
        this->_primero = nuevo;
    }
    else{
        Nodo* nuevo= new Nodo;
        Nodo* temp= (_primero->_anterior);
        (*nuevo)={elem, temp, _primero};
        temp->_siguiente= nuevo;
        _primero->_anterior= nuevo;
        _primero= nuevo;
    }
    this->_longitud= this->_longitud+1;
} 

void Lista::agregarAtras(const int& elem) {
    // Completar
    agregarAdelante(elem);
    _primero= _primero->_siguiente;
}

void Lista::eliminar(Nat i) {
    // Completar
    if(_longitud==1){
        delete _primero;
        _primero= nullptr;
    }
    else{
        Nodo* actual= _primero;
        for(int cont=0;cont<i;cont++){
            actual= actual->_siguiente;
        }
        Nodo* ant= actual->_anterior;
        Nodo* sig= actual->_siguiente;
        delete actual;

        ant->_siguiente= sig;
        sig->_anterior= ant; 

        if(i==0)
            _primero= sig;
    }
    this->_longitud= this->_longitud-1;
   
}

int Lista::longitud() const {
    // Completar
    return this->_longitud;
}

const int& Lista::iesimo(Nat i) const {
    // Completar (hint: es igual a la anterior...)
    Nodo* elem= this-> _primero;
    for (int cont = 0; cont<i; cont++){
        elem= elem-> _siguiente;
    }
    return elem-> valor;
}

int& Lista::iesimo(Nat i) {
    // Completar (hint: es igual a la anterior...)
    Nodo* elem= this-> _primero;
    for (Nat cont = 0; cont<i; cont++){
        elem= elem-> _siguiente;
    }
    return elem-> valor; 
}

void Lista::mostrar(ostream& o) {
    // Completar
}
