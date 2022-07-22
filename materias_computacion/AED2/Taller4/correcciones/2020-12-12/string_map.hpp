template <typename T>
string_map<T>::string_map(): raiz(nullptr), _size(0){
    // COMPLETAR
}

template <typename T>
string_map<T>::string_map(const string_map<T>& aCopiar) : string_map() { *this = aCopiar; } // Provisto por la catedra: utiliza el operador asignacion para realizar la copia.

template <typename T>
void string_map<T>::copiarTodosLosNodos(const Nodo* arb, Nodo* aCopiar){
    if(aCopiar != nullptr){
        Nodo* copia= new Nodo();
        arb= copia;
        for(int i=0; i<(aCopiar->siguientes).size() ;i++){
            if( (aCopiar->siguientes)[i] != nullptr ){
                Nodo* nuevo2= new Nodo();
                copiarTodosLosNodos(nuevo2,(aCopiar->siguientes)[i]);
            }
        }
    }
}


template <typename T>
string_map<T>& string_map<T>::operator=(const string_map<T>& d) {
    // COMPLETAR
    (*this).~string_map();
    Nodo* nuevo= new Nodo();
    copiarTodosLosNodos(nuevo,d.raiz);
    this->raiz= nuevo;
    return *this;
    /*for(int i=0; i< ; (raiz->siguientes).size()){

    }*/
}

template <typename T>
void string_map<T>::insert(const pair<string, T>&  elem){
    if(raiz == nullptr){
        Nodo* raiz= new Nodo();
    }

    Nodo* actual= raiz;
    for(int i=0; i<(elem.first).size() ;i++){
        if((actual->siguientes)[(elem.first)[i]] == nullptr ){
            Nodo* nuevo2= new Nodo();
            (actual->siguientes)[(elem.first)[i]] =nuevo2;
        }
        actual= (actual->siguientes)[(elem.first)[i]];
    }

    if(actual->definicion == nullptr)
        _size++;

    *(actual->definicion)= elem.second;

}

template <typename T>
void string_map<T>::borarArbol(Nodo* arb){
    if(arb != nullptr){
        for(int i=0; i<(arb->siguientes).size() ;i++){
            borarArbol((arb->siguientes)[i]);
            delete arb;
        }
    }
}

template <typename T>
string_map<T>::~string_map(){
    // COMPLETAR
    borarArbol(raiz);
}

template <typename T>
T& string_map<T>::operator[](const string& clave){
    // COMPLETAR
}


template <typename T>
int string_map<T>::count(const string& clave) const{
    // COMPLETAR
    if(raiz == nullptr)
        return 0;
    else{
        Nodo* sig= raiz->siguientes[clave[0]];
        for(int i=1; i<clave.size() && sig!=nullptr ;i++){
            sig= sig->siguientes[clave[i]];
        }
        if(raiz->definicion == nullptr)
            return 0;
        else
            return 1; 
    }
}

template <typename T>
const T& string_map<T>::at(const string& clave) const {
    // COMPLETAR
    Nodo* actual= raiz;
    for(int i=0; i<clave.size() ;i++){
        actual= actual->siguientes[clave[i]];
    }
    return actual->definicion;
}

template <typename T>
T& string_map<T>::at(const string& clave) {
    // COMPLETAR
    Nodo* actual= raiz;
    for(int i=0; i<clave.size() ;i++){
        actual= actual->siguientes[clave[i]];
    }
    return *(actual->definicion);
}

template <typename T>
void string_map<T>::erase(const string& clave) {
    // COMPLETAR
    Nodo* actual= raiz;
    for(int i=0; i<clave.size() ;i++){
        actual= actual->siguientes[clave[i]];
    }
    bool nodoInutil= true;
    for(int i=0; i<(actual->siguientes).size() ;i++){
        if ((actual->siguientes)[i] != nullptr)
            nodoInutil= false; 
    }

    if(nodoInutil)
        delete actual;
    else
        actual->definicion == nullptr;
    
    _size--;
}

template <typename T>
int string_map<T>::size() const{
    // COMPLETAR
    return _size;
}

template <typename T>
bool string_map<T>::empty() const{
    // COMPLETAR
    return (raiz == nullptr);
}