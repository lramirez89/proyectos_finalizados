from datetime import *
#punto 3: ordenar listas

#si una lista ordenada devuelvo true:
def ordenado(l):
	k=0
	while k<len(l)-1 and l[k]<=l[k+1]:
		k+=1
	return(k==len(l)-1)


#merge modificado para ordenar una lista de fechas(d) y de valores(vals)
def merge(d,vals1,vals2,vals3,vals4,i,m,j):
	#subarreglo i-m . a[m] incluido.
	l1= d[i:m+1]
	v11=vals1[i:m+1]
	v21=vals2[i:m+1]
	v31=vals3[i:m+1]
	v41=vals4[i:m+1]

	#segundo subarreglo
	l2= d[m+1:j+1]
	v12= vals1[m+1:j+1]
	v22= vals2[m+1:j+1]
	v32= vals3[m+1:j+1]
	v42= vals4[m+1:j+1]

	il1=0
	il2=0
	k=i
	while k<=j:
		if il2>=len(l2) or ((il1<len(l1)) and l1[il1]<=l2[il2]) :
			d[k]=l1[il1]
			vals1[k]=v11[il1]
			vals2[k]=v21[il1]
			vals3[k]=v31[il1]
			vals4[k]=v41[il1]
			il1+=1
		else:
			d[k]=l2[il2]
			vals1[k]=v12[il2]
			vals2[k]=v22[il2]
			vals3[k]=v32[il2]
			vals4[k]=v42[il2]
			il2+=1
		k+=1

def mergeSortIndices(d,vals1,vals2,vals3,vals4,i,j):
	if i<j:
		m= (i+j)//2
		mergeSortIndices(d,vals1,vals2,vals3,vals4,i,m)
		mergeSortIndices(d,vals1,vals2,vals3,vals4,m+1,j)
		merge(d,vals1,vals2,vals3,vals4,i,m,j)

def ordenarListasYFechas(d,vals1,vals2,vals3,vals4):
	mergeSortIndices(d,vals1,vals2,vals3,vals4, 0,len(d)-1)

# #test merge:
# a= datetime(year=1999 ,month=9 ,day=4,hour=15, minute=45,second=30)
# b= datetime(year=1999 ,month=9 ,day=3,hour=15, minute=45,second=30)
# print("ordenado:",a<b)

# d=[a,b]
# vals1=[0.3,0.9]
# vals2=[2.0,0.0]
# vals3=[100.0,98.6]
# vals4=[4.0,5.0]

# print(d)
# print(vals1,vals2,vals3,vals4)

# merge(d,vals1,vals2,vals3,vals4,0,0,1)

# print(d)
# print(vals1,vals2,vals3,vals4)
# print('\n')


# #test mergeSortIndices:
# a= datetime(year=1999 ,month=9 ,day=4,hour=15, minute=45,second=30)
# b= datetime(year=1998 ,month=9 ,day=3,hour=15, minute=45,second=30)
# print("ordenado:",a<b)

# d=[a,b]
# vals1=[0.3,0.9]
# vals2=[2.0,0.0]
# vals3=[100.0,98.6]
# vals4=[4.0,5.0]

# print(d)
# print(vals1,vals2,vals3,vals4)

# mergeSortIndices(d,vals1,vals2,vals3,vals4,0,1)

# print(d)
# print(vals1,vals2,vals3,vals4)
# print('\n')

# # test ordenarListasYFechas:
# a= datetime(year=1999 ,month=9 ,day=4,hour=15, minute=45,second=30)
# b= datetime(year=1970 ,month=9 ,day=3,hour=15, minute=45,second=30)
# c= datetime(year=1960 ,month=9 ,day=3,hour=15, minute=45,second=30)
# print("ordenado:",a<b)

# d=[a,b,c]
# vals1=[0.3,0.9,0.4]
# vals2=[2.0,0.0,0.4]
# vals3=[100.0,98.6,0.4]
# vals4=[4.0,5.0,0.4]

# print(d)
# print(vals1,vals2,vals3,vals4)

# ordenarListasYFechas(d,vals1,vals2,vals3,vals4)

# print(d)
# print(vals1,vals2,vals3,vals4)
# print('\n')