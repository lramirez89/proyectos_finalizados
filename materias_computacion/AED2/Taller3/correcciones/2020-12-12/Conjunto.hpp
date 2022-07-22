//constructor de nodo
template <class T>
Conjunto<T>::Nodo::Nodo(const T& v):valor(v),izq(nullptr),der(nullptr){}

template <class T>
Conjunto<T>::Conjunto() {
    // Completar
    _raiz= nullptr;
}

template <class T>
Conjunto<T>::~Conjunto() { 
    // Completar
    borrarArbol(_raiz );
    //borrarArbol(_raiz);
    /*unsigned int car= cardinal();
    for(unsigned int i=0 ; i< car ;i++){
        remover(maximo());
    }*/
}

template <class T>
bool Conjunto<T>::pertenece(const T& clave) const {
    Nodo* actual= _raiz;
    while(actual != nullptr && actual->valor != clave){
        if(clave < actual->valor)
            actual= actual->izq;
        else{
            actual= actual->der;
        }
    }
    return (actual != nullptr);
}

template <class T>
void Conjunto<T>::insertar(const T& clave) {
    //caso base
    int caso;
    Nodo* padre= nullptr;
    Nodo* actual= _raiz;
    while(actual != nullptr && actual->valor != clave){
        if(clave < actual->valor){
            padre= actual;
            actual= actual->izq;
            caso= 0;
        }
        else{
            padre= actual;
            actual= actual->der;
            caso= 1;
        }
    }
    if(actual == nullptr ||  actual->valor != clave){
        Nodo* nuevo= new Nodo(clave);
        if(padre == nullptr)
            _raiz= nuevo;
        else{
            if(caso == 0)
                padre->izq= nuevo;
            else
                padre->der= nuevo;
        }
    }
}

//inserta un arbol en la parte izquieda de un dado valor en un arbol de nodos
//requiere que exista dicho valor
template <class T>
void Conjunto<T>::borrarArbol(Nodo* arb){
    /*if(arb != nullptr){
        if(arb->izq != nullptr)
            borrarArbol(arb->izq);
        if(arb->der != nullptr)
            borrarArbol(arb->);
    }*/
    if(arb != nullptr){
        borrarArbol(arb->der);
        borrarArbol(arb->izq);
        delete arb;
    }
}

template <class T>
void Conjunto<T>::remover(const T& clave) {
    //encontrar el nodo a borrar
    Nodo* padre=nullptr;
    Nodo* actual= _raiz;
    int dir;             //0 si tomo el camino izquierdo y 1 si tomo el derecho
    while(actual!=nullptr && actual->valor != clave){
        if(clave < actual->valor){
            padre= actual;
            dir= 0;
            actual= actual->izq;
        }
        else{
            padre= actual;
            dir= 1;
            actual= actual->der;
        }
    }

    if(actual != nullptr){//si es nill el elemento no esta, no tengo que hacer nada
        //casos base
        if(actual->der == nullptr && actual->izq == nullptr){
            delete actual;
            if(padre == nullptr){  //si es hoja y raiz
                delete actual;
                _raiz= nullptr;
            }
            else{
                if(dir == 0)
                    padre->izq= nullptr;
                else
                    padre->der= nullptr;
            }
        }
        if(actual->der == nullptr && actual->izq != nullptr){
            Nodo* hijo= actual->izq;
            delete actual;
            if(dir=0)
                padre->izq= hijo;
            else
                padre->der= hijo;
        }
        if(actual->der != nullptr && actual->izq == nullptr){
            Nodo* hijo= actual->der;
            delete actual;
            if(dir=0)
                padre->izq = hijo;
            else
                padre->der= hijo;
        }
        //caso recursivo
        if(actual->der != nullptr && actual->izq != nullptr){
            T sig= siguiente(clave);
            Nodo* sigPtr=_raiz;
            while(sigPtr->valor != sig){
                if(sigPtr->valor < sig)
                    sigPtr= sigPtr->der;
                else
                    sigPtr= sigPtr->izq;
            }
            T swap= sigPtr->valor;
            sigPtr->valor= actual->valor;
            actual->valor= swap;
            remover(clave);
        }
    }
}

template<class T>
const T& Conjunto<T>::siguienteNodo(const Nodo* arb, const T& elem){
    //casos base
    if(elem > arb->valor && arb->der == nullptr)
        return arb->valor;
    if(elem < arb->valor && arb->izq == nullptr)
        return arb->valor;

    //casos recursivos
    if(elem > arb->valor){
        return siguienteNodo(arb->der, elem);
    }
    else{
        //T sigHastaAhora= arb->valor;
        if(arb->valor > siguienteNodo(arb->izq, elem))
            return arb->valor;
        else
            return siguienteNodo(arb->izq, elem);
    }
}

template <class T>
const T& Conjunto<T>::siguiente(const T& clave) {
    return siguienteNodo(_raiz, clave);




    /*Conjunto temp;
    if(_raiz->der == nullptr && _raiz->izq == nullptr)        //si es hoja, caso base
        return _raiz->valor;

    if(clave > _raiz->valor){
        temp._raiz= _raiz->der;
        return temp.siguiente(clave);
    }

    if(_raiz->izq != nullptr && _raiz->der != nullptr){    //en este punto es seguro que la raiz es mayor que valor
        temp._raiz= _raiz->izq;
        return temp.siguiente(clave);
    }

    if(_raiz->izq != nullptr && _raiz->der == nullptr){
        temp._raiz= _raiz->izq;
        return temp.siguiente(clave);
    }

    if(_raiz->izq == nullptr && _raiz->der != nullptr){
        if(clave > (_raiz->der)->valor){
            temp._raiz= _raiz->der;
            return temp.siguiente(clave);
        }
        else
            return _raiz->valor;
    }*/
}

template <class T>
const T& Conjunto<T>::minimo() const {
    Nodo* min= _raiz;
    while(min->izq != nullptr){
        min= min->izq;
    }
    return min->valor;
}

template <class T>
const T& Conjunto<T>::maximo() const {
    Nodo* max= _raiz;
    while(max->izq != nullptr){
        max= max->der;
    }
    return max->valor;
}

template<class T>
unsigned int Conjunto<T>::contarRecursivo(Nodo* arb) const{
    if(arb == nullptr)
        return 0;
    else{
        if(arb->izq == nullptr && arb->der == nullptr)
            return 1;
        if(arb->izq == nullptr && arb->der != nullptr)
            return 1+contarRecursivo(arb->der);
        if(arb->izq != nullptr && arb->der == nullptr)
            return 1+contarRecursivo(arb->izq);
        if(arb->izq != nullptr && arb->der != nullptr)
            return 1+contarRecursivo(arb->der)+contarRecursivo(arb->izq);
    }
}

template <class T>
unsigned int Conjunto<T>::cardinal() const {
    return contarRecursivo(_raiz);
    /*if(_raiz == nullptr)
        return 0;
    else{
        T actual= minimo();
        T ultimo= maximo();
        int count= 1;
    
        while(actual!=ultimo){
            actual= siguiente(actual);
            count++;
        }
    }

    return count;*/


    /*Conjunto<T> temp;
    Conjunto<T> temp2;
    if(_raiz == nullptr)
        return 0;
    else if(_raiz->izq == nullptr && _raiz->der == nullptr){
        return 1;
    }
    else if(_raiz->izq != nullptr && _raiz->der == nullptr){
        temp._raiz= _raiz->izq;
        return temp.cardinal()+1;
    }
    else if(_raiz->izq == nullptr && _raiz->der != nullptr){
        temp._raiz= _raiz->der;
        return temp.cardinal()+1;
    }
    else if(_raiz->izq != nullptr && _raiz->der != nullptr){
        temp._raiz= _raiz->izq;
        temp2._raiz= _raiz->der;
        return temp.cardinal()+temp2.cardinal()+1;
    }*/
}

template <class T>
void Conjunto<T>::mostrar(std::ostream&) const {
    assert(false);
}

