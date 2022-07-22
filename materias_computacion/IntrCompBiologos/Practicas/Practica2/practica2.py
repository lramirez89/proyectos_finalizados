#ejercicio 1)
# a)-------------------------------------------------------------------------------------------------------
def noesCero(n):
	return n!=0

# l=[0,1,2]
# print(noesCero(l[0]))
# print(noesCero(l[1]))
# print(noesCero(l[2]))

# b)------------------------------------------------------------------------------------------------
def iguales(n1,n2):
	res= n1==n2
	return res

# c)------------------------------------------------------------------------------------------------
def menor(n1,n2):
	res= n1<n2
	return res

# d)-----------------------------------------------------------------------------------------------
def par(n):
	res= n%2==0
	return res

#print(par(5))

# e)-------------------------------------------------------------------------------------------------
def divisible(n,d):
	res= n%d==0
	return res

# f)-----------------------------------------------------------------------------------------------
def imparDivisiblePorTresOCinco(n):
	res= n%2==1 and (n%3==0 or n%5==0)
	return res 








#ejercicio2
# a)------------------------------------------------------------------------------------------
def factorial(n):
	i= 1
	res=1
	while i<=n:
		res*= i
		i+= 1
	return res

#codigo de prueba:
# fac4= factorial(4)
# print("El factorial de 4 es",fac4)

# b)------------------------------------------------------------------------------------------------
def sumaDivisores(n):
	i=1
	res=0
	while i<=n:
		if n%i==0:
			res+= i
		i+= 1
	return res 

#codigo de prueba:
# sum5= sumaDivisores(5)
# print("La suma de los divisores de 5 es",sum5)

# c)-----------------------------------------------------------------------------------------------------

#utilizando sumaDivisores
def primo(n):
	if n<0:
		n= -n
	return sumaDivisores(n)==n+1

#codigo de prueba:
# print("primo 1:",primo(1))
# print("primo 2:",primo(2))
# print("primo 3:",primo(3))
# print("primo 4:",primo(4))
# print("primo -5:",primo(-5))
# print("primo 6:",primo(6))
# print("primo 7:",primo(7))
# print("primo -41:",primo(-41))
# print("primo 99:",primo(99))

#utilizando que si p es complejo tiene que ser divisible por un entero a lo sumo sqrt(p)
def primo2(n):
	if n<0:
		n= -n
	if n==1:
		return False
	elif n==2:
		return True
	else:  
		i=2
		while i*i<=n and n%i!=0:
			i+=1
		return n%i!=0

#codigo de prueba:
# print("primo 0:",primo2(0))
# print("primo 1:",primo2(1))
# print("primo 2:",primo2(2))
# print("primo 3:",primo2(3))
# print("primo 4:",primo2(4))
# print("primo 5:",primo2(5))
# print("primo -6:",primo2(-6))
# print("primo 7:",primo2(7))
# print("primo 8:",primo2(8))
# print("primo 9:",primo2(9))
# print("primo 10:",primo2(10))
# print("primo -11:",primo2(-11))
# print("primo 12:",primo2(12))
# print("primo 13:",primo2(13))
# print("primo 14:",primo2(14))
# print("primo 41:",primo2(41))
# print("primo 99:",primo2(99))

# d)---------------------------------------------------------------------------------------------------------
def menorDivisiblePorTres(n):
	i=n+1
	while (i%3)!=0:
		i+=1
	return i 

#codigo de prueba:
# print("Menor div por tres(2):",menorDivisiblePorTres(2))
# print("Menor div por tres(3):",menorDivisiblePorTres(3))
# print("Menor div por tres(4):",menorDivisiblePorTres(4))
# print("Menor div por tres(5):",menorDivisiblePorTres(5))
# print("Menor div por tres(6):",menorDivisiblePorTres(6))
# print("Menor div por tres(7):",menorDivisiblePorTres(7))


# e)-----------------------------------------------------------------------------------------------------------
def mayorPrimo(n1,n2):
	if not(primo(n1) and n2%n1==0):
		return False
	else:
		i=n1+1
		while i<=n2 and (not primo(i) or n2%i!=0): #a->b es -a or b : si es primo, entonces me fijo si i divide a n2
			i+=1
		return n2%i!=0                   #si sali del ciclo porque encontre otro primo devuelvo False

#codigo de prueba
# print("May prim divide(2,3):",mayorPrimo(2,3))
# print("May prim divide(5,10):",mayorPrimo(5,10))
# print("May prim divide(2,10):",mayorPrimo(2,10))
# print("May prim divide(13,26):",mayorPrimo(13,26))
# print("May prim divide(2,26):",mayorPrimo(2,26))

# f)--------------------------------------------------------------------------------------------------------------
#algoritmo de euclides (recursivo)
def mcd(n1,n2):
	if n2==0:
		return n1
	elif n2==1:
		return 1
	elif n1<n2:
		return mcd(n2,n1)
	else:
		return mcd(n2,n1%n2)

#codigo de prueba:
# print("mcd(24,0)",mcd(24,0))
# print("mcd(24,12)",mcd(24,12))
# print("mcd(12,24)",mcd(12,24))
# print("mcd(3*7*2*2=84,5*2*2=20)",mcd(84,20))

#algotirmo iterativo
def mcd2(n1,n2):
	if n1==0:
		return n2
	elif n2==0:
		return n1
	else:
		res=n2
		if n1<n2:
			res=n1
		while not(n1%res==0 and n2%res==0):
			res-=1
		return res

#codigo de prueba:
# print("mcd(24,0)",mcd2(24,0))
# print("mcd(24,12)",mcd2(24,12))
# print("mcd(12,24)",mcd2(12,24))
# print("mcd(3*7*2*2=84,5*2*2=20)",mcd(84,20))








#Ejercicio 3
# a)-----------------------------------------------------------------------------------------------------------------
def suma(a):
	res=0
	i=0
	while i<len(a):
		res+= a[i]
		i+=1
	return res 

#codigo de prueba
# print("suma[1,2,3]:",suma([1,2,3]))
# print("suma[1,3,3]:",suma([1,3,3]))

# b)-----------------------------------------------------------------------------------------------------------
def promedio(a):
	return suma(a)/len(a)

#codigo de prueba
# print("promedio([1,2,3,4]):",promedio([1,2,3,4]))

# c)-----------------------------------------------------------------------------------------------------------
def maximo(a):
	res=a[0]
	i=1
	while i<len(a):
		if a[i]>res:
			res=a[i]
		i+=1
	return res

#codigo de prueba
# print("maximo[1,2,3,122,4,2]:",maximo([1,2,3,122,4,2]))

# d)------------------------------------------------------------------------------------------------------------
def listaDeAbs(a):
	res=[]
	i=0
	while i<len(a):
		if a[i]<0:
			res.append(-a[i])
		else:
			res.append(a[i])
		i+=1
	return res 

#codigo de prueba
# print("listaDeAbs([1,-3,5,4,-122,4,3])",listaDeAbs([1,-3,5,4,-122,4,3]))


# e)------------------------------------------------------------------------------------------------------------
def todosPares(a):
	i=0
	while i<len(a) and  par(a[i]):
		i+=1
	return i==len(a)

#codigo de prueba
# print("todosPares([1,2,3,4])",todosPares([1,2,3,4]))
# print("todosPares([0,2,6,4])",todosPares([0,2,6,4]))



# f)-------------------------------------------------------------------------------------------------------------
def valAbs(x):
	if x<0:
		return -x
	else:
		return x

def maximoAbsoluto(a):
	res=  valAbs(a[0])
	i=1
	while i<len(a):
		if valAbs(a[i])>res:
			res= valAbs(a[i])
		i+=1
	return res

# #codigo de prueba:
# l=[1,2,-34,3,-22]
# print("maximoAbsoluto([1,2,-34,3,-22])",maximoAbsoluto(l))


# g)-------------------------------------------------------------------------------------------------------------
def divisores(n):
	res=[]
	i=1
	while i<=n:
		if n%i==0:
			res.append(i)
		i+=1
	return res

#codigo de prueba
# print("Divisores de 10:",divisores(10))


# h)------------------------------------------------------------------------------------------------------------
def cantidadApariciones(a,x):
	count=0
	i=0
	while i<len(a):
		if x==a[i]:
			count+=1
		i+=1
	return count

#codigo de prueba:
# l=[1,2,2,3,4,2]
# print("cantidadApariciones([1,2,2,3,4,2],2):",cantidadApariciones(l,2))
# print("cantidadApariciones([1,2,2,3,4,2],100):",cantidadApariciones(l,100))


# i)-----------------------------------------------------------------------------------------------------------
def masRepetido(a):
	res= a[0]
	i=1
	while i<len(a):
		if cantidadApariciones(a,a[i])>cantidadApariciones(a,res):
			res= a[i]
		i+=1
	return res

#codigo de prueba:
# l=[1,2,2,3,4,2]
# print("masRepetido([1,2,2,3,4,2]):",masRepetido(l))


# j)--------------------------------------------------------------------------------------------------------------
def ordenAscendente(a):
	i=0
	while i<len(a)-1 and a[i]<a[i+1]:
		i+=1
	return i==len(a)-1 or a==[]

# #codigo de prueba:
# l=[1,2,3,12,1222]
# m=[1,3,4,0,1,100]
# v=[]
# u=[1]
# d=[1,2]
# n=[2,1]
# print("ordenAscendente(l)",ordenAscendente(l))
# print("ordenAscendente(m)",ordenAscendente(m))
# print("ordenAscendente(vacio)",ordenAscendente(v))
# print("ordenAscendente(unico elemento)",ordenAscendente(u))
# print("ordenAscendente(dos elementos asc)",ordenAscendente(d))
# print("ordenAscendente(dos elementos no asc)",ordenAscendente(n))


# k)---------------------------------------------------------------------------------------------------------------
def reverso(a):
	res=[]
	i=0
	while i<len(a):
		res.append(a[len(a)-1-i])
		i+=1
	return res

#codigo de prueba:
# l=[1,2,30,4,50]
# print("reverso(l)",reverso(l))





#Ejercicio 4
# a)------------------------------------------------------------------------------------------------------------
def potencia(x,n):
	res= 1
	i=1
	while i<=n:
		res*=x
		i+=1 
	return res

def raizCuadrada(n):
	#trabajamos con enteros y luego corremos la coma: sqrt(n)*10^9 (corremos la coma diez lugares)
	#si lo metemos dentro de la raiz nos queda sqrt(n*10^18): calculamos la raiz con la parte entera y luego corremos la coma 
	n= n*potencia(10,8)  #si queremos la raiz con 4 decimales
	i=0
	while (i+1)*(i+1)<n:
		i+=1
	return i/potencia(10,4)

# #codigo de prueba
# print(raizCuadrada(2))

#version usando busqueda binaria
def raizCuadrada2(n):
	n= n*potencia(10,18)  #si queremos la raiz con 9 decimales
	i=0
	j=n
	while j!=i+1 and i!=j:
		valMedio= (i+j)//2
		if valMedio*valMedio<=n:
			i= valMedio
		else:
			j= valMedio
	return i/potencia(10,9)

#codigo de prueba
# print(raizCuadrada2(2))

# b)--------------------------------------------------------------------------------------------------------------
def sumaPosPares(a):
	i=0
	res=0
	while i<len(a):
		res+= a[i]
		i+=2
	return res

# #codigo de prueba:
# print("sumaPosPares([]):",sumaPosPares([]))
# print("sumaPosPares([2,3]):",sumaPosPares([2,3]))
# print("sumaPosPares([1,2,3,4]):",sumaPosPares([1,2,3,4]))
# print("sumaPosPares([10]):",sumaPosPares([10]))


# c)---------------------------------------------------------------------------------------------------------------
def capicua(a):
	i=0
	while i<(len(a)//2) and (a[i] == a[len(a)-1-i]):
		i+=1
	return i==(len(a)//2)

# #codigo de prueba
# print("capicua([]):",capicua([]))
# print("capicua([1,2,3]):",capicua([1,2,3]))
# print("capicua([1,2,1]):",capicua([1,2,1]))
# print("capicua([4,2,2,4]):",capicua([4,2,2,4]))
# print("capicua([4,10,2,4]):",capicua([4,10,2,4]))


# d)---------------------------------------------------------------------------------------------------------------
def promedioImpares(a):
	if len(a)<2:
		return 0
	else:
		sumaPosImpares=0
		i=1
		while i<len(a):
			sumaPosImpares+= a[i]
			i+=2
		return sumaPosImpares//(len(a)//2)

# #codigo de prueba
# print("promedioImpares([1]):",promedioImpares([1]))
# print("promedioImpares([1,2]):",promedioImpares([1,2]))
# print("promedioImpares([1,2,3]):",promedioImpares([1,2,3]))
# print("promedioImpares([1,2,3,4]):",promedioImpares([1,2,3,4]))


# e)----------------------------------------------------------------------------------------------------------------
def minimo(a):
	i=1
	minimo= a[0]
	while i<len(a):
		if minimo>a[i]:
			minimo= a[i]
		i+=1
	return minimo

#codigo de prueba:
# print("minimo([2])",minimo([2]))
# print("minimo([1,-2,3,4])",minimo([1,-2,3,4]))
# print("minimo([1,3,0])",minimo([1,3,0]))

# f)------------------------------------------------------------------------------------------------------------
def tamanioDeLaMayorSublistaTodosIguales(a):
	res=1
	i=0
	j=1
	while j<len(a)-1:
		j+=1
		if a[i]==a[j-1]:
			if res<j-i:
				res=j-i
		else:  #a[i]!=a[j-1]
			i=j-1
	return res


#codigo de prueba:
print("tamDeLaMaySublisTodIg([1,2,3,3,3,4,5,5,5,5,6]):",tamanioDeLaMayorSublistaTodosIguales([1,2,3,3,3,4,5,5,5,5,6]))
print("tamDeLaMaySublisTodIg([1,2,3,3,4,5,6]):",tamanioDeLaMayorSublistaTodosIguales([1,2,3,3,4,5,6]))
print("tamDeLaMaySublisTodIg([1,2,1,2,1,2]):",tamanioDeLaMayorSublistaTodosIguales([1,2,1,2,1,2]))
print("tamDeLaMaySublisTodIg([1,12,12,12,12,9,9]):",tamanioDeLaMayorSublistaTodosIguales([1,12,12,12,12,9,9]))
print("tamDeLaMaySublisTodIg([2,2,2]):",tamanioDeLaMayorSublistaTodosIguales([2,2,2]))
print("tamDeLaMaySublisTodIg([1,2,3,3,3]):",tamanioDeLaMayorSublistaTodosIguales([1,2,3,3,3]))



























