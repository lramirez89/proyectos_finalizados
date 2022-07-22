from random import randrange
import matplotlib.pyplot as plt
import numpy as np
import time
from mini3 import *
import sys
sys.setrecursionlimit(1000000000)

f= open("resultados.txt","a")

def listaAleatoria(tamanio,rango):
	np_array = np.random.randint(low=0, high=rango,size=tamanio)
	listita = list(np_array)
	return listita

def sort(a):
	a.sort()

#tamanios: una lista con los tamanios de listas aleatorias que voy a implementar
tamanios=[]
i=1
while i<=3:
	tamanios.append(10*(10**i))
	i+=1


#------------------- implmenento funciones utiles------------------------------------------------------------------------------
def medirTiempos(lfun,l,resultados):
	for i in range(len(lfun)):
		lc=l[:]
		start=time.time()
		lfun[i](lc)
		end=time.time()
		resultados[i].append(end-start)

def medTiemDistLisAleatorias(lfun,resultados,tamanios,rango):
	for i in range(len(tamanios)):
		l=listaAleatoria(tamanios[i],rango)
		medirTiempos(lfun,l,resultados)





#------------------llamo a mis funciones para medir tiempos------------------------------------------------------------------

# lfun=[upSortSlice,upSortIndex,bubleSort,mergeSortSlices,mergeSortIndex,mergeSortIndexv2,quickSortCopy,quickSortIndex,sort]

# resupsortSlice=[]
# resupSortIndex=[]
# resbubleSort=[]
# resmergeSortSlices=[]
# resmergeSortIndex=[]
# resmergeSortIndexv2=[]
# resquickSortCopy=[]
# resquickSortIndex=[]
# ressort=[]

# resultados=[resupsortSlice,resupSortIndex,resbubleSort,resmergeSortSlices,resmergeSortIndex,resmergeSortIndexv2,resquickSortCopy,resquickSortIndex,ressort]

# medTiemDistLisAleatorias(lfun,resultados,tamanios,100)





# ## escribo los resultados en un archivo:
# f.write("Tamanios:")
# f.write(str(tamanios))
# f.write('\n\n')

# f.write("Resultados:\n")
# for i in range(len(resultados)):
# 	f.write(str(resultados[i]))
# 	f.write('\n')
# f.write('\n')
# f.close()










# #----------------- pruebo con 10e4 y 10e5 para las tres funciones de mejor rendimiento------------------------------------------------------------------------
# lfun=[mergeSortIndexv2,quickSortIndex,sort]

# resmergeSortSlices=[]
# resmergeSortIndex=[]
# resmergeSortIndexv2=[]
# resquickSortCopy=[]
# resquickSortIndex=[]
# ressort=[]

# resultados=[resmergeSortIndexv2,resquickSortIndex,ressort]

# tamanios=[100000,1000000] #cien mil

# medTiemDistLisAleatorias(lfun,resultados,tamanios,100)
# f.write("Tamanios:")
# f.write(str(tamanios))
# f.write('\n\n')

# f.write("Resultados:\n")
# for i in range(len(resultados)):
# 	f.write(str(resultados[i]))
# 	f.write('\n')
# f.write('\n')
# f.close()





#----------------- pruebo con 10e6 para las dos funciones de mejor rendimiento------------------------------------------------------------------------
lfun=[mergeSortIndexv2,quickSortIndex,sort]

ressort=[]

resultados=[ressort]

tamanios=[10000000]

medTiemDistLisAleatorias(lfun,resultados,tamanios,100)
f.write("Tamanios:")
f.write(str(tamanios))
f.write('\n\n')

f.write("Resultados:\n")
for i in range(len(resultados)):
	f.write(str(resultados[i]))
	f.write('\n')
f.write('\n')
f.close()













