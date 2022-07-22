import random
import itertools

#1)---------------------------------------------------------------------------------------------------------
def generarMazo():
	m=[1,2,3,4,5,6,7,10,11,12,1,2,3,4,5,6,7,10,11,12,1,2,3,4,5,6,7,10,11,12,1,2,3,4,5,6,7,10,11,12]
	random.shuffle(m)
	return m

#codigo de prueba:
# m= generarMazo()
# print(m,'\n')

#2)----------------------------------------------------------------------------------------------------------
def repartir (mazo, jug1, jug2, jug3, jug4):
	#le doy 3 cartas a jug1
	jug1.append(mazo[0])
	jug1.append(mazo[1])
	jug1.append(mazo[2])

	#le doy 3 cartas a jug2
	jug2.append(mazo[3])
	jug2.append(mazo[4])
	jug2.append(mazo[5])

	#le doy 3 cartas a jug3
	jug3.append(mazo[6])
	jug3.append(mazo[7])
	jug3.append(mazo[8])

	#le doy 3 cartas a jug4
	jug4.append(mazo[9])
	jug4.append(mazo[10])
	jug4.append(mazo[11])

	mazo_resultado=[]
	i=12
	while i<len(mazo):
		mazo_resultado.append(mazo[i])
		i+=1

	return mazo_resultado

#codigo de prueba:
# m= generarMazo()
# jug1=[]
# jug2=[]
# jug3=[]
# jug4=[]

# print(m)
# print("jug1:",jug1)
# print("jug2:",jug2)
# print("jug3:",jug3)
# print("jug4:",jug4,'\n')

# res=repartir(m,jug1,jug2,jug3,jug4)
# print("mazo original:",m)
# print("mazo devuelto:",res)
# print("jug1:",jug1)
# print("jug2:",jug2)
# print("jug3:",jug3)
# print("jug4:",jug4,'\n')



#3)---------------------------------------------------------------------------------------------------------
def iniciarMesa(mazo, mesa):
	elem= mazo.pop(0)
	mesa.append(elem)
	elem= mazo.pop(0)
	mesa.append(elem)
	elem= mazo.pop(0)
	mesa.append(elem)
	elem= mazo.pop(0)
	mesa.append(elem)

#codigo de prueba
# m= generarMazo()
# mesa=[]
# print(m)
# print("mesa:",mesa,'\n')

# iniciarMesa(m,mesa)
# print(m)
# print("mesa:",mesa,'\n')


# 4)-------------------------------------------------------------------------------------------------------
def subListas(lista):
	"""
	arma una lista de todas las sublistas de la lista dada
	"""

	resultado= []
	for k in range (1, len(lista)+1):
		for listita in itertools.combinations(lista, k):
			resultado.append(list(listita))
	return resultado

#suma los valores de cada carta
def sumaListas(lista):
	suma= 0
	i= 0
	while i<len(lista):
		if lista[i]!=10 and lista[i]!=11 and lista[i]!=12:
			suma+= lista[i]
		else:
			suma+= lista[i]-2
		i+=1 
	return suma

def swapearElementos(i,j,lista):
	#a=a+b  
	#b=a-b 
	#a=a-b 
	lista[i]= lista[i]+lista[j] 
	lista[j]= lista[i]- lista[j]
	lista[i]= lista[i]- lista[j]


def juegosPosibles(jug, mesa):
	res= []
	sublisMesas= subListas(mesa)
	i= 0                                #indice de jug
	j= 0                                #indice de mesa
	while i<len(jug):
		while j<len(sublisMesas):
			if sumaListas(sublisMesas[j])==(15-jug[i]):
				sublisMesas[j].append(jug[i])
				#swapeo el primero con el último elemento
				swapearElementos(0, len(sublisMesas[j])-1, sublisMesas[j])
				#añado el juego al resultado
				res.append(sublisMesas[j])
			j+= 1
		i+= 1

	return res

#codigo de prueba
# jugador=[5,6,7]
# mesa=[4,2,12,5,5,4,4,3]
# print("jugador:",jugador)
# print("mesa:",mesa)

# juegos= juegosPosibles(jugador,mesa)
# print("juegos posibles:",juegos,'\n')



#5)----------------------------------------------------------------------------------------------------------
def elegirMejor(juegos):
	mejor= 0                  #indice al mejor juego
	i= 1
	while i<len(juegos):
		if len(juegos[i])>len(juegos[mejor]):
			mejor= i 
		i+= 1
	return juegos[mejor]

#codigo de prueba
# juegos=[[5,5,5],[10,5],[4,3,3,4,1],[7,8]]
# print("juegos:",juegos)

# mejor= elegirMejor(juegos)
# print("mejor juego:",mejor,'\n')


#6)-------------------------------------------------------------------------------------------------------------
def eliminar1raAparicion(elem,lista):
	i=0
	while i<len(lista) and lista[i]!=elem:
		i+= 1
	if i<len(lista):
		lista.pop(i)

# def eliminarUltraAparicion(elem,lista):
# 	i=len(lista)-1
# 	while i>=0 and lista[i]!=elem:
# 		i-=1

# 	while i>0:
# 		lista[i]= lista[i-1]
# 		i-=1
# 	lista.pop(0)

# lista=[1,2,3,4]
# eliminarUltraAparicion(1,lista)
# print(lista)


def jugar(mesa, jug, basa):
	if juegosPosibles(jug,mesa)!=[] :
		mejorJuego= elegirMejor(juegosPosibles(jug,mesa))

		#elimino las cartas de la mesa y la del jugador
		i=1                              								#el primer elemento es la carta del jugador
		while i<len(mejorJuego):
			eliminar1raAparicion(mejorJuego[i],mesa)
			i+= 1
		eliminar1raAparicion(mejorJuego[0],jug)

		#agrego el juego a la basa
		basa.append(mejorJuego)
	else:
		mesa.append(jug[0])
		jug.pop(0)

#codigo de prueba:
# jugador=[5,6,7]
# mesa=[4,2,12,5,5,4,4,3]
# basa=[]
# print("jugador:",jugador)
# print("mesa:",mesa)
# print("basa:",basa,'\n')

# juegos= juegosPosibles(jugador,mesa)
# print("juegos posibles:",juegos,'\n')

# jugar(mesa,jugador,basa)
# print("jugador:",jugador)
# print("mesa:",mesa)
# print("basa:",basa,'\n')

#7)----------------------------------------------------------------------------------------------------------
def jugarRonda(mesa, jug1, basa1, jug2, basa2, jug3, basa3, jug4, basa4):
	ronda=1
	while ronda<=3:
		jugar(mesa,jug1,basa1)
		jugar(mesa,jug2,basa2)
		jugar(mesa,jug3,basa3)
		jugar(mesa,jug4,basa4)
		ronda+= 1

#codigo de prueba
# mesa=[]
# jug1=[]
# jug2=[]
# jug3=[]
# jug4=[]
# basa1=[]
# basa2=[]
# basa3=[]
# basa4=[]
# mazo= generarMazo()
# iniciarMesa(mazo,mesa)
# repartir(mazo, jug1, jug2, jug3, jug4)
# print("mesa:",mesa)
# print("jug1:",jug1,basa1,"jug2:",jug2,basa2,"jug3:",jug3,basa3,"jug4:",jug2,basa4,'\n')

# jugarRonda(mesa, jug1, basa1, jug2, basa2, jug3, basa3, jug4, basa4)

# print("Despues de jugar la ronda:")
# print("mesa:",mesa,)
# print("jug1:",jug1,basa1,"jug2:",jug2,basa2,"jug3:",jug3,basa3,"jug4:",jug2,basa4)




#8)----------------------------------------------------------------------------------------------------
def elementosTotalesListasDeListas(lista):
	res= 0
	i= 0
	while i<len(lista):
		res+= len(lista[i])
		i+= 1
	return res

def sumaPuntos(basa1, basa2, basa3, basa4):
	res=[0,0,0,0]

	puntaje1= elementosTotalesListasDeListas(basa1)
	puntaje2= elementosTotalesListasDeListas(basa2)
	puntaje3= elementosTotalesListasDeListas(basa3)
	puntaje4= elementosTotalesListasDeListas(basa4)

	if puntaje1>puntaje2 and puntaje1>puntaje3 and puntaje1>puntaje4:
		res[0]+= 1
	elif puntaje2>puntaje1 and puntaje2>puntaje3 and puntaje2>puntaje4:
		res[1]+= 1
	elif puntaje3>puntaje2 and puntaje3>puntaje1 and puntaje3>puntaje4:
		res[2]+= 1
	elif puntaje4>puntaje2 and puntaje4>puntaje3 and puntaje4>puntaje1:
		res[3]+= 1

	return res

#codigo de prueba
# basa1=[[1],[2]]
# basa2=[[1,2,3],[4,5,6,4,2]]
# basa3=[[1],[2,3]]
# basa4=[[1],[2,1],[1],[1]]
# puntajes= sumaPuntos(basa1,basa2,basa3,basa4)
# print("Puntajes basa2 gana:",puntajes)

# basa1=[[1],[2]]
# basa2=[[1,2,3],[4,5,6,4,2]]
# basa3=[[9,9,9],[4,5,6,4,2]]
# basa4=[[1],[2,1],[1],[1]]
# puntajes= sumaPuntos(basa1,basa2,basa3,basa4)
# print("Puntajes empate:",puntajes)

#9)------------------------------------------------------------------------------------------------------------
def programaPrincipal(mazo,mesa,jug1,basa1,jug2,basa2,jug4,basa4):
	iniciarMesa(mazo, mesa)

	while len(mazo)!=0:
		mazo=repartir(mazo,jug1,jug2,jug3,jug4)
		jugarRonda(mesa, jug1, basa1, jug2, basa2, jug3, basa3, jug4, basa4)

	if sumaPuntos(basa1, basa2, basa3, basa4)[0]==1:
		ganador= "jug1"
	elif sumaPuntos(basa1, basa2, basa3, basa4)[1]==1:
		ganador= "jug2"
	elif sumaPuntos(basa1, basa2, basa3, basa4)[2]==1:
		ganador= "jug3"
	elif sumaPuntos(basa1, basa2, basa3, basa4)[3]==1:
		ganador= "jug4"
	else:
		ganador= "Empate"

	return ganador



mazo= generarMazo()
print("mazo:",mazo,'\n')
jug1=[]
basa1=[]

jug2=[]
basa2=[]

jug3=[]
basa3=[]

jug4=[]
basa4=[]

mesa= []


ganador= programaPrincipal(mazo,mesa,jug1,basa1,jug2,basa2,jug4,basa4)

print("basa1:",basa1)
print("basa2:",basa2)
print("basa3:",basa3)
print("basa4:",basa4,'\n')

print("El ganador es:",ganador,'\n')


#programaPrincipal()

#10)
#corro el programa muchas veces: espero que cada jugador gane la misma cantidad de veces
# cantVecesGanoJug1= 0
# cantVecesGanoJug2= 0
# cantVecesGanoJug3= 0
# cantVecesGanoJug4= 0
# cantEmpates= 0

# i= 0
# while i<1000:
# 	m= generarMazo()
# 	jug1=[]
# 	basa1=[]

# 	jug2=[]
# 	basa2=[]

# 	jug3=[]
# 	basa3=[]

# 	jug4=[]
# 	basa4=[]

# 	mesa= []

# 	ganador= programaPrincipal(m,mesa,jug1,basa1,jug2,basa2,jug4,basa4)
# 	if ganador=="jug1":
# 		cantVecesGanoJug1+=1
# 	elif ganador=="jug2":
# 		cantVecesGanoJug2+=1
# 	elif ganador=="jug3":
# 		cantVecesGanoJug3+=1
# 	elif ganador=="jug4":
# 		cantVecesGanoJug4+=1
# 	else:
# 		cantEmpates+= 1
# 	i+=1

# porcentajeGano1= (cantVecesGanoJug1/i)*100
# porcentajeGano2= (cantVecesGanoJug2/i)*100
# porcentajeGano3= (cantVecesGanoJug3/i)*100
# porcentajeGano4= (cantVecesGanoJug4/i)*100
# porcentajeEmpates= (cantEmpates/i)*100

# print("jug 1: gano el ",porcentajeGano1,"% de las veces")
# print("jug 2: gano el ",porcentajeGano2,"% de las veces")
# print("jug 3: gano el ",porcentajeGano3,"% de las veces")
# print("jug 4: gano el ",porcentajeGano4,"% de las veces")
# print("el porcentaje de empates es ",porcentajeEmpates)







