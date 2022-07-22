template <typename T>
string_map<T>::string_map() : raiz(new string_map::Nodo()), _size(0){};

template <typename T>
string_map<T>::Nodo::Nodo() : siguientes(256, nullptr), definicion(nullptr){};

template <typename T>
string_map<T>::Nodo::Nodo(T *def) : siguientes(256, nullptr), definicion(def){};

template <typename T>
string_map<T>::~string_map()
{
    deleteWithChildren(raiz);
}

template <typename T>
void string_map<T>::deleteWithChildren(Nodo *actual)
{
    for (int i = 0; i < 256; i++)
    {
        if (actual->siguientes[i] != nullptr)
        {
            deleteWithChildren(actual->siguientes[i]);
        }
    }
    delete (actual->definicion);
    delete (actual);
}

template <typename T>
void string_map<T>::insert(const pair<string, T> &par)
{
    Nodo *it = raiz;

    string clave = par.first;
    T *valor = new T(par.second);

    for (char c : clave)
    {
        if (it->siguientes[int(c)] == nullptr)
        {
            Nodo *nuevo = new string_map::Nodo();
            it->siguientes[int(c)] = nuevo;
        }
        it = it->siguientes[int(c)];
    }

    // Si estamos redefiniendo un valor primero hay que liberar lo que habia antes
    if (it->definicion != nullptr)
    {
        delete (it->definicion);
    }
    else
    {
        // Solo aumentamos la cantidad de elementos si la insercion es nueva
        _size++;
    }
    it->definicion = valor;
}

// Funcion auxiliar, compartida por at (version constante) y count
template <typename T>
typename string_map<T>::Nodo *string_map<T>::search(const string &clave) const
{
    Nodo *it = raiz;

    for (char c : clave)
    {
        if (it->siguientes[int(c)] == nullptr)
        {
            return nullptr;
        }
        it = it->siguientes[int(c)];
    }
    return it;
}

template <typename T>
T &string_map<T>::at(const string &clave)
{
    Nodo *it = raiz;

    for (char c : clave)
    {
        it = it->siguientes[int(c)];
    }
    return *it->definicion;
}

template <typename T>
const T &string_map<T>::at(const string &clave) const
{
    Nodo *buscado = search(clave);
    return buscado->definicion;
}

template <typename T>
int string_map<T>::count(const string &clave) const
{
    Nodo *buscado = search(clave);
    if (buscado == nullptr or buscado->definicion == nullptr)
    {
        return 0;
    }
    return 1;
}

template <typename T>
string_map<T>::string_map(const string_map<T> &aCopiar) : string_map()
{
    *this = aCopiar;
} // Provisto por la catedra: utiliza el operador asignacion para realizar la copia.

template <typename T>
string_map<T> &string_map<T>::operator=(const string_map<T> &d)
{
    // Liberamos la memoria de lo que hubiera antes
    deleteWithChildren(raiz);

    raiz = new string_map::Nodo();
    copyChildren(raiz, d.raiz);
    _size = d._size;

    return *this;
}

template <typename T>
void string_map<T>::copyChildren(Nodo *actCopia, Nodo *actD)
{
    for (int i = 0; i < 256; i++)
    {
        if (actD->siguientes[i] != nullptr)
        {
            // Vamos a hacer una copia nodo a nodo. Para evitar aliasing no deseado, asignamos nuevo espacio de memoria
            Nodo *nuevo = new string_map::Nodo();
            Nodo *hijoActD = actD->siguientes[i];

            if (hijoActD->definicion != nullptr)
            {
                // Asi como cree un nuevo nodo, tambien tengo que copiar la definicion
                nuevo->definicion = new T(*hijoActD->definicion);
            }

            actCopia->siguientes[i] = nuevo;
            copyChildren(nuevo, hijoActD);
        }
    }
}

template <typename T>
void string_map<T>::erase(const string &clave)
{
    vector<char> vecClave = vector<char>(clave.begin(), clave.end());
    deleteNonRelevantNodes(raiz, vecClave, 0);
}

template <typename T>
bool string_map<T>::deleteNonRelevantNodes(Nodo *actual, vector<char> &vecClave, int i)
{
    // Caso base (Llegamos donde queremos borrar el significado)
    if (i == vecClave.size())
    {
        delete (actual->definicion);
        actual->definicion = nullptr;
        _size--;
        // Solo borramos el nodo si era hoja
        if (irrelevantNode(actual))
        {
            delete (actual);
            return true;
        }
        return false;
    }
    else
    {
        // Ya sabemos donde bucar, por precondicion la clave esta definida
        Nodo *nextOnPath = actual->siguientes[int(vecClave[i])];
        bool deletedNext = deleteNonRelevantNodes(nextOnPath, vecClave, i + 1);

        // Recordar que cuando borramos algo, tenemos que setearlo a nullptr para avisarle al padre
        if (deletedNext)
        {
            actual->siguientes[int(vecClave[i])] = nullptr;
        }

        // Subiendo en la recusion, nos fijamos is los borrados anteriores hicieron irrelevante al nodo
        if (irrelevantNode(actual))
        {
            // Consideramos que el arbol siempre tiene que tener la raiz(es el unico nodo que puede ser "irrelevante")
            if (actual != raiz)
            {
                delete (actual);
            }
            return true;
        }
        return false;
    }
}

template <typename T>
bool string_map<T>::irrelevantNode(Nodo *actual)
{
    // Un nodo es irrelevante, cuando no tiene asignado un valor o...
    bool irrelevant = true;
    if (actual->definicion != nullptr)
    {
        irrelevant = false;
    }
    else
    {
        //... cuando no forma parte de ningun camino hacia otro valor
        for (int i = 0; i < 256; i++)
        {
            if (actual->siguientes[i] != nullptr)
            {
                irrelevant = false;
            }
        }
    }
    return irrelevant;
}

template <typename T>
int string_map<T>::size() const
{
    return _size;
}

template <typename T>
bool string_map<T>::empty() const
{
    return _size == 0;
}

template <typename T>
T &string_map<T>::operator[](const string &clave)
{
    /*Si no estaba definida la clave, la creamos nosotros.
    Le asignamos el valor por definicion de la clase T, no va a quedar "irrelevante"
    porque el operador [] viene acompañado de un igual para asignar un valor */
    if (count(clave) == 0)
    {
        insert(make_pair(clave, *new T()));
    }

    // Referencia modificable para asignarle un nuevo valor a esa clave
    return at(clave);
}
