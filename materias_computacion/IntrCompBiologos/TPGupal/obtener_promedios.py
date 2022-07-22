from datetime import *


# punto 5: creación de función obtener_promedios

def calcularPromedioEntreIndices(l,i,j):
	cantElemValidos=0
	k=i
	suma=0
	while k<=j:
		if l[k]!='NaN':
			suma+=l[k]
			cantElemValidos+=1
		k+=1
	if cantElemValidos!=0:
		return suma/cantElemValidos
	else:
		return 0


def obtener_promedios(fechas,semanas,datos1,datos2,datos3,datos4):
	iniSemanas=[]
	promedios1=[]
	promedios2=[]
	promedios3=[]
	promedios4=[]
	for i in range(len(semanas)):
		iniSemanas.append(fechas[semanas[i][0]])
		promedios1.append(calcularPromedioEntreIndices(datos1,semanas[i][0],semanas[i][len(semanas[i])-1]))
		promedios2.append(calcularPromedioEntreIndices(datos2,semanas[i][0],semanas[i][len(semanas[i])-1]))
		promedios3.append(calcularPromedioEntreIndices(datos3,semanas[i][0],semanas[i][len(semanas[i])-1]))
		promedios4.append(calcularPromedioEntreIndices(datos4,semanas[i][0],semanas[i][len(semanas[i])-1]))
	return [iniSemanas,promedios1,promedios2,promedios3,promedios4]


#test obtener_promedios
# a= datetime(year=1999 ,month=9 ,day=4,hour=15, minute=45,second=30)
# b= datetime(year=1970 ,month=9 ,day=3,hour=15, minute=45,second=30)
# c= datetime(year=1960 ,month=9 ,day=3,hour=15, minute=45,second=30)
# fechas=[c,b,a]
# semanas=[[0,1,2]]
# datos1=[1,3,6]
# datos2=[1,2,3]
# datos3=[0,1,2]
# datos4=[2,3,4]

# res=obtener_promedios(fechas,semanas,datos1,datos2,datos3,datos4)
# print(res)

