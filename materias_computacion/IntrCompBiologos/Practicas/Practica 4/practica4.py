# 1)...................................................................................................................
# a)
def fact(n):
	if n==0:
		return 1
	else:
		return n*fact(n-1)

print("factorial 1:",fact(1))
print("factorial 2:",fact(2))
print("factorial 3:",fact(3))
print("factorial 4:",fact(4))
print('\n')


# b)
def fib(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return fib(n-1)+fib(n-2)

print("fib 4:",fib(4))
print("fib 5:",fib(5))
print("fib 6:",fib(6))
print('\n')

# c)
def sumatoriaPotenciaDeDos(n1,n2):
	if n2<n1:
		return 0
	else:
		return (2**n2)+sumatoriaPotenciaDeDos(n1,n2-1)

print("sumaPot 1 1:",sumatoriaPotenciaDeDos(1,1))
print("sumaPot 1 3:",sumatoriaPotenciaDeDos(1,3))
print("sumaPot 2 4:",sumatoriaPotenciaDeDos(2,4))
print("sumaPot 0 -5:",sumatoriaPotenciaDeDos(0,-5))
print('\n')


# d)
def sumaImpares(n):
	if n==0:
		return 0
	elif n%2==1:
		return sumaImpares(n-1)
	else:
		return (n-1)+sumaImpares(n-2)

print("suma impares 1:",sumaImpares(1))
print("suma impares 2:",sumaImpares(2))
print("suma impares 3:",sumaImpares(3))
print("suma impares 4:",sumaImpares(4))
print("suma impares 5:",sumaImpares(5))
print("suma impares 6:",sumaImpares(6))
print("\n")

# e)
def sumaDigitos(n):
	if n<10:
		return n
	else:
		return (n%10)+sumaDigitos(n//10)

print("sumaDigitos 56:",sumaDigitos(56))
print("sumaDigitos 12:",sumaDigitos(12))
print("sumaDigitos 211:",sumaDigitos(211))
print('\n')


# f)
def sumaDivisores(n):
	return sumaDivisoresHasta(n,n)

def sumaDivisoresHasta(n,a):
	if a==0:
		return 0
	elif n%a==0:
		return a+sumaDivisoresHasta(n,a-1)
	else:
		return sumaDivisoresHasta(n,a-1)

print("suma divisores 5:",sumaDivisores(5))
print("suma divisores 7:",sumaDivisores(7))
print("suma divisores 10:",sumaDivisores(10))
print('\n')

# g)
def divisiblePor3(n):
	if n<10:
		return (n==3 or n==6 or n==9)
	else:
		return divisiblePor3(sumaDigitos(n))

print("divPor3 3:",divisiblePor3(3))
print("divPor3 6:",divisiblePor3(6))
print("divPor3 9:",divisiblePor3(9))
print("divPor3 12:",divisiblePor3(12))
print("divPor3 33:",divisiblePor3(33))
print("divPor3 23:",divisiblePor3(23))
print("divPor3 77:",divisiblePor3(77))
print("divPor3 129:",divisiblePor3(129))
print("\n")

# h)
def divisiblePor17(n):
	if n<0:
		n=-n
	if n<=17:
		return n==17 or n==0
	else:
		return divisiblePor17(n//10 -  (n%10)*5)

print("div17 17:",divisiblePor17(17))
print("div17 34:",divisiblePor17(34))
print("div17 51:",divisiblePor17(51))
print("div17 68:",divisiblePor17(68))
print("div17 119:",divisiblePor17(119))
print("div17 187:",divisiblePor17(187))
print("div17 20:",divisiblePor17(20))
print("div17 100:",divisiblePor17(100))
print("\n")





#............................................................................................................................
# 2)........................................................................................................................
# a)
def suma(a):
	if len(a)==0:
		return 0
	else:
		return a[0]+suma(a[1:])

print("suma([])",suma([]))
print("suma([12])",suma([12]))
print("suma([1,2,3])",suma([1,2,3]))
print('\n')


# b)
def maximo(a):
	if len(a)==1:
		return a[0]


	maxl= maximo(a[1:])
	if a[0]>maxl:
		return a[0]
	return maxl 

print("maximo([1,2,3])",maximo([1,2,3]))
print("maximo([1,2,98,0,-1])",maximo([1,2,98,0,-1]))
print("maximo([-2,4,1])",maximo([-2,4,1]))
print('\n')


# c)
def promedio(a):
	return suma(a)/len(a)

print("promedio([1,2,3])",promedio([1,2,3]))
print("promedio([1,2,98,0,-1])",promedio([1,2,98,0,-1]))
print("promedio([-2,4,1])",promedio([-2,4,1]))
print('\n')


# d)
def listaDeAbs(a):
	if len(a)==0:
		return []

	res= listaDeAbs(a[:len(a)-1])
	if a[len(a)-1]<0:
		res.append(-a[len(a)-1])
	else:
		res.append(a[len(a)-1])
	return res

print("listaDeAbs([1,2])",listaDeAbs([1,2]))
print("listaDeAbs([])",listaDeAbs([]))
print("listaDeAbs([-5,-4])",listaDeAbs([-5,-4]))
print("listaDeAbs([0,-10])",listaDeAbs([0,-10]))
print("listaDeAbs([-3,-1,-4,-5])",listaDeAbs([-3,-1,-4,-5]))
print("\n")


# e)
def maximoAbsoluto(a):
	return maximo(listaDeAbs(a))

print("maximoAbsoluto([1,2,-123,0])",maximoAbsoluto([1,2,-123,0]))
print("maximoAbsoluto([1,2,5,2])",maximoAbsoluto([1,2,5,2]))
print('\n')


# f)
def cambioDeBase(n,x):
	if n<x:
		return [n]
	else:
		return cambioDeBase(n//x,x)+[n%x]

print("cambioDeBase(256, 2):",cambioDeBase(256, 2))
print("cambioDeBase(149, 2):",cambioDeBase(149, 2))
print('\n')


# g)
def cantApariciones(a,x):
	if len(a)==0:
		return 0
	elif a[0]==x:
		return 1+cantApariciones(a[1:],x)
	else:
		return cantApariciones(a[1:],x)

print("cantApariciones([1,2,1,1],1)",cantApariciones([1,2,1,1],1))
print("cantApariciones([1,2,1,1],2)",cantApariciones([1,2,1,1],2))
print("cantApariciones([1,2,1,1],40)",cantApariciones([1,2,1,1],40))
print('\n')


# h)
def eliminar(a,i):
	if i==0:
		return a[1:]
	else:
		return [a[0]]+ eliminar(a[1:],i-1)

print("eliminar([1,2,3,4],2)",eliminar([1,2,3,4],2))
print("eliminar([1,2,3,4],3)",eliminar([1,2,3,4],3))
print("\n")


# i)
def buscarYEliminar(a,x):
	if len(a)==0:
		return []
	if a[0]==x:
		return buscarYEliminar(a[1:],x)
	else:
		return [a[0]]+buscarYEliminar(a[1:],x)

print("buscarYEliminar([1,2,3,2,1,2],2)",buscarYEliminar([1,2,3,2,1,2],2))
print('\n')


# j)
def todosPares(a):
	if len(a)==0:
		return True
	else:
		return (a[0]%2==0) and todosPares(a[1:])

print("todosPares([2,4,6,8])",todosPares([2,4,6,8]))
print("todosPares([2,4,7,8])",todosPares([2,4,7,8]))
print('\n')


# k)
def ordenAscendente(a):
	if len(a)<=1:
		return True
	else:
		return (a[0]<=a[1]) and ordenAscendente(a[1:])

print("ordenAscendente([1,2,4])",ordenAscendente([1,2,4]))
print("ordenAscendente([1,2,2])",ordenAscendente([1,2,2]))
print("ordenAscendente([1,2,1])",ordenAscendente([1,2,1]))
print('\n')


# l)
def reverso(a):
	if len(a)==0:
		return []
	else:
		return [a[len(a)-1]]+reverso(a[:len(a)-1])

print("reverso(['h','o','l','a']):",reverso(['h','o','l','a']))
print("reverso(reverso(['h','o','l','a'])):",reverso(reverso(['h','o','l','a'])))
print("reverso([]):",reverso([]))
print("reverso([1]):",reverso([1]))
print('\n')

# m)
def sumaPosImpares(a):
	if len(a)<=0:
		return 0
	elif len(a)%2==1:
		return sumaPosImpares(a[:len(a)-1])
	else:
		return a[len(a)-1]+sumaPosImpares(a[:len(a)-1])

print("sumaPosImpares([3,5,4,3,2]):",sumaPosImpares([3,5,4,3,2]))
print("sumaPosImpares([3,5,4,3]):",sumaPosImpares([3,5,4,3]))
print("sumaPosImpares([]):",sumaPosImpares([]))
print("sumaPosImpares([1]):",sumaPosImpares([1]))
print("sumaPosImpares([1,2]):",sumaPosImpares([1,2]))
print('\n')


# n)
def triangular(a):
	if len(a)<=1:
		return True
	elif a[len(a)-1]<=a[len(a)-2]:
		return triangular(a[:len(a)-1])
	else:
		return ordenAscendente(a[:len(a)-1])

print("triangular([1,2,3,3,3]):",triangular([1,2,3,3,3]))
print("triangular([1,2,1,2]):",triangular([1,2,1,2]))
print("triangular([1]):",triangular([1]))
print("triangular([1,2,3,4,5]):",triangular([1,2,3,4,5]))
print("triangular([4,3,2]):",triangular([4,3,2]))
print("triangular([]):",triangular([]))
print("triangular([1,10,9,8,7]):",triangular([1,10,9,8,7]))
print("triangular([1,10,9,10,7]):",triangular([1,10,9,10,7]))
print("triangular([1,2,3,2,0]):",triangular([1,2,3,2,0]))
print('\n')






#........................................................................................................................
# 3)......................................................................................................................
# a)
def map(fn,a):
	if len(a)==0:
		return []
	else:
		return [fn(a[0])]+map(fn,a[1:])

print("map(fact,[1,2,3])",map(fact,[1,2,3]))
print("map(reverso,[[1,2],[3,4],[]])",map(reverso,[[1,2],[3,4],[]]))
print('\n')


# b)
def filter(fn,a):
	if len(a)==0:
		return []
	elif fn(a[0]):
		return [a[0]]+filter(fn,a[1:])
	else:
		return filter(fn,a[1:])

print("filter(divisiblePor3, [1,2,3,4,5,6])",filter(divisiblePor3, [1,2,3,4,5,6]))
print("filter(todosPares,[[1,2],[2,6],[4,5],[]])",filter(todosPares,[[1,2],[2,6],[4,5],[]]))
print('\n')


# c)
def suma2(x,y):
	return x+y

def reduce(fn,a):
	if len(a)==1:
		return a[0]
	else:
		return fn(a[0],reduce(fn,a[1:]))

print("reduce(suma2,[1,2,3,4]):",reduce(suma2,[1,2,3,4]))
print("\n")


# d)
def sumaV2(a):
	if len(a)==0:
		return 0
	else:
		return reduce(suma2,a)

print("suma([])",sumaV2([]))
print("suma([12])",sumaV2([12]))
print("suma([1,2,3])",sumaV2([1,2,3]))
print('\n')

#-----------------------------------------------
def maximoEntreDos(x,y):
	if x>y:
		return x 
	else:
		return y 

def maximoV2(a):
	return reduce(maximoEntreDos,a)

print("maximo([1,2,3])",maximoV2([1,2,3]))
print("maximo([1,2,98,0,-1])",maximoV2([1,2,98,0,-1]))
print("maximo([-2,4,1])",maximoV2([-2,4,1]))
print('\n')

#--------------------------------------------------------------------
def cantAparicionesV2(a,x):
	def igualaX(elem):
		return elem==x 

	return len(filter(igualaX,a))

print("cantAparicionesV2([1,2,1,1],1)",cantAparicionesV2([1,2,1,1],1))
print("cantAparicionesV2([1,2,1,1],2)",cantAparicionesV2([1,2,1,1],2))
print("cantAparicionesV2([1,2,1,1],40)",cantAparicionesV2([1,2,1,1],40))
print('\n')

#otra version
def esIgualAX(x):
	def esIgualAY(y):
		return y==x 
	return esIgualAY

def cantAparicionesV3(a,x):
	return len(filter(esIgualAX(x),a))

print("cantAparicionesV3([1,2,1,1],1)",cantAparicionesV3([1,2,1,1],1))
print("cantAparicionesV3([1,2,1,1],2)",cantAparicionesV3([1,2,1,1],2))
print("cantAparicionesV3([1,2,1,1],40)",cantAparicionesV3([1,2,1,1],40))
print('\n')

#----------------------------------------------------------------------------------------
def esPar(x):
	return x%2==0

def todosParesV2(a):
	return len(filter(esPar,a))==len(a)

print("todosPares([2,4,6,8])",todosParesV2([2,4,6,8]))
print("todosPares([2,4,7,8])",todosParesV2([2,4,7,8]))
print('\n')

#-----------------------------------
def ordenAscendenteV2(a):
	def menorQueElSiguiente(i):
		return (i>len(a)-2) or a[i]<=a[i+1]

	return len(filter(menorQueElSiguiente,list(range(len(a)))))==len(a)

print("ordenAscendente([1,2,4])",ordenAscendenteV2([1,2,4]))
print("ordenAscendente([1,2,2])",ordenAscendenteV2([1,2,2]))
print("ordenAscendente([1,2,1])",ordenAscendenteV2([1,2,1]))
print("ordenAscendente([])",ordenAscendenteV2([]))
print("ordenAscendente([3])",ordenAscendenteV2([3]))
print("ordenAscendente([3,2])",ordenAscendenteV2([3,2]))
print("ordenAscendente([2,3])",ordenAscendenteV2([2,3]))
print('\n')






#...............................................................................................................................
# 4)
# a)
def A(a,i):
	if i<0:
		return 0
	else:
		return (a[i]//abs(a[i])) * abs(a[i]**i) + A(a,i-1)

print("A([1,-2,3,-4],3):",A([1,-2,3,-4],3))
print("A([1,-2,3,-4],2):",A([1,-2,3,-4],2))
print("A([1,-2,3,-4],1):",A([1,-2,3,-4],1))
print("A([1,-2,3,-4],0):",A([1,-2,3,-4],0))
print('\n')


# b)
def primo(n):
	return sumaDivisores(n)== n+1

def B(n1,n2):
	if primo(n1+1):
		return n1+1 
	else:
		return B(n1+1,n2)

print("B(1,5):",B(1,5))
print("B(2,5):",B(2,5))
print("B(4,10):",B(4,10))
print("B(10,20):",B(10,20))
print("B(4,5):",B(4,5))
print('\n')


#---------- otra version----------------------------------------------------------
#devuelve el menor primo entre x y los elementos que estan entre n1 y n2
def primoMasChicoEntre(x,n1,n2):
	if n1 >= n2:
		return x
	elif primo(n2) and n2<x:
		return primoMasChicoEntre(n2,n1,n2-1)
	else:
		return primoMasChicoEntre(x,n1,n2-1)


def Bv2(n1,n2):
	return primoMasChicoEntre(n2,n1,n2)

print("B(1,5):",Bv2(1,5))
print("B(2,5):",Bv2(2,5))
print("B(4,10):",Bv2(4,10))
print("B(10,20):",Bv2(10,20))
print("B(4,5):",Bv2(4,5))
print('\n')

#------ otra version--------------------------------------------------------------------------------
#devuelvo el primo mas chico de una lista. Requiere que haya primo y lista ordenada
def primoMenor(a):
	if primo(a[0]):
		return a[0]
	else:
		return primoMenor(a[1:])

def Bv3(n1,n2):
	return primoMenor(list(range(n1+1,n2+1)))

print("B(1,5):",Bv3(1,5))
print("B(2,5):",Bv3(2,5))
print("B(4,10):",Bv3(4,10))
print("B(10,20):",Bv3(10,20))
print("B(4,5):",Bv3(4,5))
print('\n')



# c)
#implemento C hasta el indice i inclusive
def Chastai(a,b,i):
	if i<0:
		return []
	else:
		return Chastai(a,b,i-1)+[a[i]+b[i%len(b)]]

def C(a,b):
	return Chastai(a,b,len(a)-1)

print("C([1,2,3,4,5],[4,5]):",C([1,2,3,4,5],[4,5]))
print("C([],[4,5]):",C([],[4,5]))
print("C([2],[4,5]):",C([2],[4,5]))
print('\n')


# d)
def pert(v,elem):
	return cantApariciones(elem,v)!=0

#X-V
def D(x,v):
	if len(x)==0:
		return []
	elif pert(x[0],v):
		return D(x[1:],v)
	else:
		return [x[0]]+ D(x[1:],v)

print("D([1,2,10,20],[1,4,2,4,5]):",D([1,2,10,20],[1,4,2,4,5]))
print("D([],[1,4]):",D([],[1,4]))
print("D([2],[]):",D([2],[]))
print('\n')





#...............................................................................................................................
# 5)
# a)
def busquedaBinariaAcotada(a,i,j,x):
	if i>=j:
		return False
	if j==i+1:
		return x==a[i]
	if a[(i+j)//2] <= x:
		return busquedaBinariaAcotada(a,(i+j)//2,j,x)
	else:
		return busquedaBinariaAcotada(a,i,(i+j)//2,x)

print("busquedaBinariaAcotada([1,2,3,4],0,4,3):",busquedaBinariaAcotada([1,2,3,4],0,4,3))
print("busquedaBinariaAcotada([1,2,3,4],2,4,3):",busquedaBinariaAcotada([1,2,3,4],2,4,3))
print("busquedaBinariaAcotada([1,2,3,4],0,2,3):",busquedaBinariaAcotada([1,2,3,4],0,2,3))
print("busquedaBinariaAcotada([1,2,3,4],0,4,1):",busquedaBinariaAcotada([1,2,3,4],0,4,1))
print("busquedaBinariaAcotada([1,2,3,4],0,4,4):",busquedaBinariaAcotada([1,2,3,4],0,4,4))
print("busquedaBinariaAcotada([1,2,3,4],0,4,10):",busquedaBinariaAcotada([1,2,3,4],0,4,10))
print("busquedaBinariaAcotada([1],0,1,1):",busquedaBinariaAcotada([1],0,1,1))
print("busquedaBinariaAcotada([1,2,3,4],4,0,3):",busquedaBinariaAcotada([1,2,3,4],4,0,3))
print('\n')


# b)
def merge(a,b):
	if len(a)==0 and len(b)==0:
		return []
	if len(b)==0 or (len(a)>0 and a[0]<=b[0]):
		return [a[0]]+ merge(a[1:],b)
	else:
		return [b[0]]+ merge(a,b[1:])

print("Test merge:")
print("merge([1,3,5],[2,4,6])",merge([1,3,5],[2,4,6]))
print('\n')

def mergeSort(a):
	if len(a)==0:
		return []
	elif len(a)==1:
		return [a[0]]
	else:
		return merge(mergeSort(a[0:len(a)//2]),mergeSort(a[len(a)//2:len(a)]))

print("Test mergeSort:")
print("mergeSort([7,4,0,6,7]):",mergeSort([7,4,0,6,7]))
print("mergeSort([]):",mergeSort([]))
print("mergeSort([1,2,3,4]):",mergeSort([1,2,3,4]))
print("mergeSort([5,4,3]):",mergeSort([5,4,3]))
print("\n")




# c)
def menores(a,x):
	if len(a)==0:
		return []
	elif a[0]<x:
		return [a[0]]+menores(a[1:],x)
	else:
		return menores(a[1:],x)

def mayoresOIg(a,x):
	if len(a)==0:
		return []
	elif a[0]>=x:
		return [a[0]]+mayoresOIg(a[1:],x)
	else:
		return mayoresOIg(a[1:],x)

def quickSort(a):
	if len(a)==0:
		return []
	if len(a)==1:
		return [a[0]]
	else:
		return quickSort(menores(a[1:],a[0]))+[a[0]]+quickSort(mayoresOIg(a[1:],a[0]))

print("test quickSort:")
print("quickSort([4,3,2,1]):",quickSort([4,3,2,1]))
print("quickSort([4]):",quickSort([4]))
print("quickSort([]):",quickSort([]))
print("quickSort([5,6,7]):",quickSort([5,6,7]))
print("quickSort([5,6,5,1]):",quickSort([5,6,5,1]))
print('\n')



# d)
# si la sublista entre i y j inclusive esta rotada. Requiere !=[] y 0<=i<=j<len(a) y a rotado (segun enunciado)
# no es igual al "auxiliar" de la especificacion, en este caso k==0 se considera no rotado
def rotado(a,i,j):
	return a[i]>a[j]

def minimoRotadoSubl(a,i,j):
	if i==j:
		return a[i]

	if rotado(a,i,(i+j)//2):
		return minimoRotadoSubl(a,i,(i+j)//2)
	if rotado(a,(i+j)//2 +1,j):
		return minimoRotadoSubl(a,(i+j)//2 +1,j)
	if (not rotado(a,i,(i+j)//2)) and (not rotado(a,(i+j)//2 +1,j)):
		if a[i]<a[(i+j)//2 +1]:
			return minimoRotadoSubl(a,i,(i+j)//2)
		else:
			return minimoRotadoSubl(a,(i+j)//2 +1,j)

def minimoRotado(a):
	return minimoRotadoSubl(a,0,len(a)-1)

print("test minimoRotado:")
print("minimoRotado([8,10,1,4,4,5]):",minimoRotado([8,10,1,4,4,5]))
print("minimoRotado([2]):",minimoRotado([2]))
print("minimoRotado([1,2,3,-1]):",minimoRotado([1,2,3,-1]))
print("minimoRotado([5,6,7]):",minimoRotado([5,6,7]))


































