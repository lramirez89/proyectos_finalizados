#include <iostream>

using namespace std;

using uint = unsigned int;

// Pre: 0 <= mes < 12
uint dias_en_mes(uint mes) {
    uint dias[] = {
        // ene, feb, mar, abr, may, jun
        31, 28, 31, 30, 31, 30,
        // jul, ago, sep, oct, nov, dic
        31, 31, 30, 31, 30, 31
    };
    return dias[mes - 1];
}

// Ejercicio 7, 8, 9 y 10

// Clase Fecha
class Fecha {
  public:
    // Completar declaraciones funciones
    #if EJ >= 9 // Para ejercicio 9
    bool operator==(Fecha o);
    #endif

    Fecha(int mes, int dia);
    int mes();
    int dia();
    void incrementar_dia();
  private:
    //Completar miembros internos
    int mes_;
    int dia_;
};

Fecha::Fecha(int m, int d){
    if(m>=1 && m<=12){
        mes_= m;
    }
    if(dias_en_mes(m)>=d && d>=1){
        dia_= d;
    }
}

int Fecha::mes(){
    return mes_;
}

int Fecha::dia(){
    return dia_;
}

ostream& operator<<(ostream& os, Fecha f){
    os << f.dia()<< "/"<< f.mes();
}

#if EJ >= 9
bool Fecha::operator==(Fecha o) {
    bool igual_dia = this->dia() == o.dia();
    // Completar iguadad (ej 9)
    bool igual_mes = mes() == o.mes();
    return igual_dia && igual_mes;
}
#endif

void Fecha::incrementar_dia(){
    if(dia()<dias_en_mes(mes()))
        dia_++;
    else{
        dia_=1;
        mes_++;
    }
}

// Ejercicio 11, 12

// Clase Horario
class Horario{
    public:
        Horario(uint hora, uint minuto);
        uint hora();
        uint min();
        bool operator==(Horario h);
        bool operator<(Horario h);
    private:
        uint hora_;
        uint min_;
};

Horario::Horario(uint h, uint m){
    hora_=h;
    min_=m;
}

uint Horario::hora(){
    return hora_;
}

uint Horario::min(){
    return min_;
}

ostream& operator<<(ostream& os, Horario h){
    os << h.hora() << ":" << h.min();
}

bool Horario::operator==(Horario o){
    return hora()==o.hora() && min()==o.min();
}
/*bool Horario::operator==(Horario o) {
    bool igual_hora = this->hora() == o.hora();
    bool igual_min = min() == o.min();
    return igual_hora && igual_min;
}*/

bool Horario::operator<(Horario h){
    return hora()<h.hora() || (hora()==h.hora() && min()<h.min());
}
// Ejercicio 13
// Clase Recordatorio

class Recordatorio{
    public:
        Recordatorio(Fecha fech, Horario hor, string mens);
        string mensaje();
        Fecha fecha();
        Horario horario();
    private:
        string mensaje_;
        Fecha f_;
        Horario h_;
};

Recordatorio::Recordatorio(Fecha f, Horario h, string m):f_(f), h_(h), mensaje_(m){}
string Recordatorio::mensaje(){
    return mensaje_;
}

Fecha Recordatorio::fecha(){
    return f_;
}

Horario Recordatorio::horario(){
    return h_;
}

ostream& operator<<(ostream& os, Recordatorio r){
    os << r.mensaje()<< " @ " << r.fecha() << " " << r.horario();
    return os;
}

// Ejercicio 14
// Clase Agenda
class Agenda{
    public:
        Agenda(Fecha fecha_inicial);
        void agregar_recordatorio(Recordatorio rec);
        void incrementar_dia();
        vector<Recordatorio> recordaorios_de_hoy();
        Fecha hoy();
    private:
        vector<Recordatorio> recordatorios_;
        Fecha hoy_;
};

Agenda::Agenda(Fecha fecha_inicial):hoy_(fecha_inicial), recordatorios_(){}
void Agenda::agregar_recordatorio(Recordatorio rec){
    recordatorios_.push_back(rec);
}
void Agenda::incrementar_dia(){
    hoy_.incrementar_dia();
}
/*vector<Recordatorio> Agenda::recordaorios_de_hoy(){
    vector<Recordatorio> res;
    for(Recordatorio r: recordatorios_){
        if(r.fecha()==hoy())
            res.push_back(r);
    }
    return res;
}*/
Fecha Agenda::hoy(){
    return hoy_;
}


vector<Recordatorio> Agenda::recordaorios_de_hoy(){
    vector<Recordatorio> res;
    for(Recordatorio r: recordatorios_){
        if(r.fecha()==hoy())
            res.push_back(r);
    }

    //ordenar res
    for (int i=1; i<res.size(); i++){
        for (int j=0 ; j<res.size() - 1; j++){
            if (res[j+1].horario()<res[j].horario()){
                Recordatorio temp = res[j];
                res[j] = res[j+1];
                res[j+1] = temp;
            }
        }
    }

    return res;
}


ostream& operator<<(ostream& os, Agenda a){
    os << a.hoy()<<endl;
    os << "====="<<endl;
    for(Recordatorio r: a.recordaorios_de_hoy()){
        os<< r <<endl;
    }
    return os;
}



