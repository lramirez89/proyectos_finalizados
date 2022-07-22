# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 10:38:34 2021

@author: R2D2
"""
#tp Toxico 
import csv         # para trabajar con archivos csv
import numpy as np 
import folium
from datetime import datetime, date, time, timezone, timedelta
from ordenar import ordenarListasYFechas, ordenado
from obtener_promedios import obtener_promedios
import matplotlib.pyplot as plt

#punto 1: implementar la función convertir fecha que tome el contenido de las dos primeras columnas (procesando fila por fila, 
# es decir, recibe dos cadenas de caracteres), y devuelva la fecha-hora como valor (no como cadena de caracteres).


#Abrimos el archivo 'calidad-aire.csv', y creamos dos listas con los valeres correspondientes a las 'fechas de medicion' y la 'hora de medición.


fecha_medicion=[]
hora_medicion=[]



with open('calidad-aire.csv', 'rt') as archivo:
    filas = csv.reader(archivo)
    encabezado = next(filas) #guarda la primera fila. 'next' comando que hace un paso de la iteración y devuelve esa fila
    #print('Encabezado:')
    #print(encabezado)
    #print('Filas:')
    for fila in filas:
        fecha=fila[0]
        hora=fila[1]
        fecha_medicion.append(fecha)
        hora_medicion.append(hora)
#print(hora_medicion)


#ver si es el mismo lrgo en las listas:
#print(len(fecha_medicion))
#print(len(hora_medicion))

#definimos la funcion:

def convertir_fechas(fecha_medicion,hora_medicion):
    fechas =[]
    i=0
    while i< len(fecha_medicion):
        var1=datetime.strptime(fecha_medicion[i], '%d%b%Y:%H:%M:%S') #para que cambie el formato de la columna 1 de un string a un formato de fecha
        var2=timedelta(hours=int(hora_medicion[i]))
        var3=var1+var2 #le agrega la hora al formato de fechas
        fechas.append(var3)
        i=i+1
    return fechas

#generacion de la lista con formato fecha-hora
fechas=convertir_fechas(fecha_medicion,hora_medicion)

#veo si fechas esta ordeado (usar despues de usar funcion 'ordenado'?):
# print(ordenado(fechas))

#print(nuevo)    


#punto 2: generar listas NO2_centenario, NO2_cordoba, NO2_boca y NO2_palermo, con los valores de mediciones, y el llenado de 'NaN' para datos no válidos.
NO2_centenario=[]
NO2_cordoba=[]
NO2_boca=[]
NO2_palermo=[]
# cuando abrimos archivo, usamos excepciones ('try', 'except') al guardar los valores de las mediciones en las listas, y aquellos valores no válidos, como 'NaN'.
with open('calidad-aire.csv', 'rt') as archivo: 
    filas = csv.reader(archivo)
    encabezado = next(filas) 
    for fila in filas:
        centenario=fila[3]
        cordoba=fila[6]
        boca=fila[9]
        palermo=fila[12]
        try:
            NO2_centenario.append(int(centenario))
        except:
            NO2_centenario.append('NaN')
        try:
            NO2_cordoba.append(int(cordoba))
        except:
            NO2_cordoba.append('NaN')
        try:
            NO2_boca.append(int(boca))
        except:
            NO2_boca.append('NaN')
        try:
            NO2_palermo.append(int(palermo))
        except:        
            NO2_palermo.append('NaN')
        
# #algunos print que probamos.        
# print(len(encabezado))        
# print(len(NO2_centenario))
# print(len(NO2_cordoba))
# print(NO2_boca[0:9])
# print(NO2_palermo[0])


#punto 3
ordenarListasYFechas(fechas,NO2_centenario,NO2_boca,NO2_boca,NO2_palermo) #en otro archivo

#testeo si fechas esta ordenado
# print(ordenado(fechas))


# punto 4: 
# definir la función extraer_semanas() que tome una lista de fechas y agrupe los índices de la lista fechas por semana. Debe devolver una lista de listas, 
# donde cada lista corresponda con los índices de cada semana. Las semanas empiezan en Lunes y las fechas previas al primer lunes deben descartarse.    
    
    
# print(nuevo[0].weekday()) #Devuelve el día de la semana como un número entero, donde el lunes es 0 y el domingo es 6. Por ejemplo , un miércoles.
# print(nuevo[0].isocalendar()) #Devolver una tupla llamado objeto con tres componentes: year, weeky weekday (en esta función, lunes se define =1).
# print(nuevo[0].day)
# print(date(nuevo[0]).ctime())

#creación de la función para saber cuál lunes empieza, y cual sería el i (semana) de incio:
    
def funcion_inicio(lista):
    i=0
    while i<len(lista) and lista[i].weekday()!=0:
        i=i+1
    if i==len(lista):
        print('no hay lunes')
    else: 
        valor_inicio=i
    return valor_inicio
    
#print(funcion_inicio(nuevo))
            
   
#requiere: existe al menos un lunes
#función extraer_semanas, que agrupa las fechas por semanas:
    
def extraer_semanas(fechas):
    i=funcion_inicio(fechas)
    
    semanas=[] 
    semanas.append([i])
    i+=1

    while i<len(fechas):
        # varia=fechas[i].isocalendar()
        if fechas[i-1].isocalendar()[1]==fechas[i].isocalendar()[1]: #verifico igualdad del numero de semana
           semanas[len(semanas)-1].append(i)
        
        if fechas[i-1].isocalendar()[1]!=fechas[i].isocalendar()[1]:
            semanas.append([i])
        i=i+1
    return semanas


# va=extraer_semanas(fechas)   
# print(va[4]) 
# print(va[4:10])
        
    

#punto 5: generar los promedios semanales. Para esto, vamos a programar una función que se llame obtener promedios que tome la lista de
# fechas, la lista de semanas y las cuatro listas con datos de NO2 de las estaciones, y genere cinco listas.

#en otro archivo

semanas= extraer_semanas(fechas)
res=obtener_promedios(fechas,semanas,NO2_centenario,NO2_cordoba,NO2_boca,NO2_palermo) 
# print(res)




fechasInicioSemanas=res[0]
prom_NO2_centenario=res[1]
prom_NO2_cordoba=res[2]
prom_NO2_boca=res[3]
prom_NO2_palermo=res[4]

#listas:    
# print(fechasInicioSemanas)    
# print(prom_NO2_centenario)
# print(prom_NO2_cordoba)
# print(prom_NO2_boca)
# print(prom_NO2_palermo)   

# verificacion de que todas las listas tienen la misma longitud 

# print(len(fechasInicioSemanas))
# print(len(prom_NO2_centenario))
# print(len(prom_NO2_cordoba))
# print(len(prom_NO2_boca))
# print(len(prom_NO2_palermo))    



#punto 6: mapa

#coordenadas de las estaciones, y las estaciones:
latitud=np.array([-34.62525848, -34.6066081, -34.59956434, -34.58345295])
longitud=np.array([-58.36637351, -58.43207177, -58.39155289, -58.40535987])
estaciones=['LA BOCA','CENTENARIO', 'CORDOBA', 'PALERMO']
#arrays de las listas para calcular los promedios
# latitud.mean()
# longitud.mean()

#punto medio para ingresar en el mapa
punto_medio=[-34.6037209675,-58.39883951]





#Localización del mapa
mapa=folium.Map(location=[-34.6037209675,-58.39883951], zoom_start=10,color='green',  width=500, height=300 )
folium.CircleMarker(location=[-34.62525848, -58.36637351], radius=10,color='green', popup='La Boca', tooltip='La Boca').add_to(mapa)
folium.CircleMarker(location=[-34.6066081, -58.43207177], radius=10, color='green',popup='Centenario', tooltip='Centenario').add_to(mapa)
folium.CircleMarker(location=[-34.59956434, -58.39155289], radius=10,color='green', popup='Córdoba', tooltip='Córdoba').add_to(mapa)
folium.CircleMarker(location=[-34.58345295, -58.40535987], radius=10,color='green', popup='Palermo', tooltip='Palermo').add_to(mapa)
mapa




#punto 7: función con la generacion de mapas con los valores de los promedios semananales. En caso de datos nulos, el marker es distinto
def generar_mapa(semanas,NO2_centenario,NO2_cordoba,NO2_boca,NO2_palermo):
    i=0
    while i<len(semanas):
        mapa=folium.Map(location=[-34.6037209675,-58.39883951], zoom_start=10,color='green',  width=800, height=500 )
        #para estacion Centenario
        if NO2_centenario[i]==0:
            folium.Circle(location=[-34.6066081, -58.43207177], radius=500,color='blue', popup='Centenario', tooltip="'"'N/A'"'").add_to(mapa)
        else:   
            folium.CircleMarker(location=[-34.6066081, -58.43207177], radius=NO2_centenario[i],color='green', popup='Centenario', tooltip='Centenario').add_to(mapa)
         #para estacion Cordoba
        if NO2_cordoba[i]==0:
            folium.Circle(location=[-34.59956434, -58.39155289], radius=500,color='blue', popup='Cordoba', tooltip="'"'N/A'"'").add_to(mapa)
        else:
            folium.CircleMarker(location=[-34.59956434, -58.39155289], radius=NO2_boca[i],color='green', popup='Córdoba', tooltip='Córdoba').add_to(mapa)
        #para estacion La Boca
        if NO2_boca[i]==0:
            folium.Circle(location=[-34.62525848, -58.36637351], radius=500,color='blue', popup='La Boca', tooltip="'"'N/A'"'").add_to(mapa)
        else:
            folium.CircleMarker(location=[-34.62525848, -58.36637351], radius=NO2_boca[i],color='green', popup='La Boca', tooltip='La Boca').add_to(mapa)
        #para estacion Palermo
        if NO2_palermo[i]==0:
            folium.Circle(location=[-34.58345295, -58.40535987], radius=500,color='blue', popup='Palermo', tooltip="'"'N/A'"'").add_to(mapa)
        else:
            folium.CircleMarker(location=[-34.58345295, -58.40535987], radius=NO2_palermo[i],color='green', popup='Palermo', tooltip='Palermo').add_to(mapa)
        mapa.save("./mapas/mapaSemana"+str(i+1)+".html") #guardamos cada uno de los mapas
        i=i+1
    return 

generar_mapa(semanas,prom_NO2_centenario,prom_NO2_cordoba,prom_NO2_boca,prom_NO2_palermo)




#punto 8.  gráficos de la variación del promedio de óxidos de nitrógeno en función del tiempo (usando matplotlib)



lista_semanas=[]
i=1
while i<=len(semanas):
    lista_semanas.append(i)
    i+=1
print(len(semanas))
print(lista_semanas)


fig = plt.figure(figsize=(20,20),dpi=150)
plt.xlabel("tiempo(semanas)")
plt.ylabel("grado de contaminacion")
plt.plot(lista_semanas,prom_NO2_centenario,label="prom_NO2_centenario")
plt.plot(lista_semanas,prom_NO2_cordoba,label="prom_NO2_cordoba")
plt.plot(lista_semanas,prom_NO2_boca,label="prom_NO2_boca")
plt.plot(lista_semanas,prom_NO2_palermo,label="prom_NO2_palermo")



plt.legend(loc='best')
plt.show()


#punto 9. Estación sin funcionar:
# print(prom_NO2_centenario.count(0)) #rta 51
# print(prom_NO2_cordoba.count(0)) #rta 5
# print(prom_NO2_boca.count(0)) #rta78
# print(prom_NO2_palermo.count(0))   #rta 634
# por lo tanto, la estacion que tuvo el sensor mas tiempo sin funcionar fue la de Palermo (también se puede ver eso en el gráfico del punto 8)

