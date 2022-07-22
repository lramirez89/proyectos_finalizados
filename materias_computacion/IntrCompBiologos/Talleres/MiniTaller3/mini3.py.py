# Mini taller N 3

# 1)..............................................................................................................
	#Requiere a no vacía. Devuelvo el indice del maximo
def maximo(a):
	maximo= 0
	i=1
	while i<len(a):
		if a[i]>a[maximo]:
			maximo= i
		i+=1 
	return maximo

def upSortSliceCopia(a):
	if len(a)<=1:
		return a
	else:
		m=maximo(a)
		return upSortSliceCopia(a[0:m]+a[m+1:len(a)])+ [a[m]]

def upSortSlice(a):
	copia= upSortSliceCopia(a)
	for i in range(len(a)):
		a[i]=copia[i]


# 2)..................................................................................................................
def maximoHasta(a,j):
	maximo= 0
	i= 1
	while i<=j:
		if a[i]>a[maximo]:
			maximo= i
		i+=1
	return maximo

def upSortIndex(a):
	for j in range(len(a)):
		a[len(a)-1-j], a[maximoHasta(a,len(a)-1-j)] = a[maximoHasta(a,len(a)-1-j)], a[len(a)-1-j]


# 3)......................................................................................................................
 # "burbujeo" a y de paso devuelvo si a esta ordenado o no
def burbujear(a):
	count=0
	for i in range(len(a)-1):
		if a[i+1]<a[i]:
			a[i+1], a[i] = a[i], a[i+1]
			count+=1
	return count==0

def bubleSort(a):
	ordenado= False
	while not ordenado:
		ordenado= burbujear(a)

#--------------burbujear leve modificacion------------------------------------------------------------------------------------
def burbujearHasta(a,j):
	count=0
	for i in range(j):
		if a[i+1]<a[i]:
			a[i+1], a[i] = a[i], a[i+1]
			count+=1
	return count==0

def bubleSortl(a):
	ordenado= False
	j= len(a)-1
	while not ordenado:
		ordenado= burbujearHasta(a,j)
		j-=1



# 4)........................................................................................................................
def merge(a,b):
	if len(a)==0 and len(b)==0:
		return []
	if len(b)==0 or (len(a)>0 and a[0]<=b[0]):
		return [a[0]]+ merge(a[1:],b)
	else:
		return [b[0]]+ merge(a,b[1:])

#devuelvo una copia de la lista original
def mergeSort(a):
	if len(a)==0:
		return []
	elif len(a)==1:
		return [a[0]]
	else:
		return merge(mergeSort(a[0:len(a)//2]),mergeSort(a[len(a)//2:len(a)]))


#modifico la lista original como lo pide el enunciado
def mergeSortSlices(a):
	copia= mergeSort(a)
	for i in range(len(a)):
		a[i]=copia[i]


# 5)..........................................................................................................................
	#Igual a unirProlijo de la practica 2
def mergeIt(lis1,lis2):
	i=0
	j=0
	res=[]
	while not(i==len(lis1) and j==len(lis2)):
		if j==len(lis2) or (i<len(lis1) and lis1[i]<lis2[j]):
			res.append(lis1[i])
			i+=1
		else:
			res.append(lis2[j])
			j+=1
	return res 


#requiere 0<=i<=j<|a|
def mergeSorEntIndices(a,i,j):
	if i>j:
		return []
	if j==i:
		return [a[i]]
	else:
		return merge(mergeSorEntIndices(a,i,(i+j)//2),mergeSorEntIndices(a,(i+j)//2 +1,j))

def mergeSortIndex(a):
	copia=mergeSorEntIndices(a,0,len(a)-1)
	for i in range(len(a)):
		a[i]=copia[i]

#............. mergeSort mejor version..............................................................................
def mergev2(a,i,m,j):
	#subarreglo i-m . a[m] incluido.
	l1= a[i:m+1]

	#segundo subarreglo
	l2= a[m+1:j+1]

	il1=0
	il2=0
	k=i
	while k<=j:
		if il2>=len(l2) or ((il1<len(l1)) and l1[il1]<=l2[il2]) :
			a[k]=l1[il1]
			il1+=1
		else:
			a[k]=l2[il2]
			il2+=1
		k+=1

def mergeSortIndices(a,i,j):
	if i<j:
		m= (i+j)//2
		mergeSortIndices(a,i,m)
		mergeSortIndices(a,m+1,j)
		mergev2(a,i,m,j)

def mergeSortIndexv2(a):
	mergeSortIndices(a,0,len(a)-1)


# 6).....................................................................................................................
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

#pivote: a[0]
def quickSort(a):
	if len(a)==0:
		return []
	if len(a)==1:
		return [a[0]]
	else:
		return quickSort(menores(a[1:],a[0]))+[a[0]]+quickSort(mayoresOIg(a[1:],a[0]))

#modifoco la lista origilal como lo pide el enunciado
def quickSortCopy(a):
	copia= quickSort(a)
	for i in range(len(a)):
		a[i]=copia[i]


# 7)..................................................................................................................
def buscarMayor(a,i,j,valor):
	while a[i]<=valor and i<j:
		i+=1
	return i 

def buscarMenor(a,i,j,valor):
	while a[j]>valor and i<j:
		j-=1
	return j

def colocarPivote(a,i,j):
	pivote= i
	while i!=j:
		a[i], a[j] = a[j], a[i]
		i=buscarMayor(a,i,j,a[pivote])
		j=buscarMenor(a,i,j,a[pivote])
	if a[i]>a[pivote]:
		i-=1
	a[pivote], a[i] = a[i], a[pivote]
	return i

# def maximo: linea 5

def quickSortSublis(a,i,j):
	if j>i:
		pivote= colocarPivote(a,i,j)   
		quickSortSublis(a,i,pivote-1)
		quickSortSublis(a,pivote+1,j)

def quickSortIndex(a):
	if len(a)>=2:
		#busco el maximo y lo coloco al final
		m=maximo(a)
		a[len(a)-1], a[m] = a[m], a[len(a)-1]
		quickSortSublis(a,0,len(a)-2)    #el ultimo elemento ya esta ordenado


#-------------------- version mas sencilla-------------------------------------------------------------------------------------------------
def colocarEnPosicion(a,i,j):
	pivote=i
	posicion=0
	posMenores=0
	for i in range(len(a)):
		if a[i]<=a[pivote]:
			a[posMenores]
			posMenores+=1
	a[pivote],a[posMenores-1] = a[posMenores-1],a[pivote]
	return posMenores

def quickSortSublis2(a,i,j):
	if j>i:
		pivote= colocarEnPosicion(a,i,j)   
		quickSortSublis(a,i,pivote-1)
		quickSortSublis(a,pivote+1,j)


def quickSortIndex2(a):
	if len(a)>=2:
		quickSortSublis(a,0,len(a)-1)    #el ultimo elemento ya esta ordenado

























