
# 1)-------------------------------------------------------------------------------------------------------------
def cantSub(lis,sublis):
	res=0
	for i in range(len(lis)-len(sublis)+1):
		if haySublisEnPos(lis,sublis,i):
			res+=1
	return res

def haySublisEnPos(lis,sublis,i):
	k=0
	while k<len(sublis) and lis[i+k]==sublis[k]:
		k+=1
	return k==len(sublis)

c= "¡Vienen los zombies!, no quiero que un zombie se coma mi brazo, porque sino me volvere un zombie que come otro brazo"
resultado= cantSub(c,"zombie")
print(resultado)		

d= "nananananan"
res= cantSub(d,"nana")
print(res)

e= "dsafafa Agua"
res2= cantSub(e, "Agua")
print("Este:",res2)

#--------------- version recursiva------------------------------------------------------------------------------------
def cantSub(lis,sublis):
	return cantSubHasta(lis,sublis,len(lis)-len(sublis))

def cantSubHasta(lis,sublis,i):
	if i<0:
		return 0
	elif haySublisEnPosr(lis,sublis,i):
		return 1+ cantSubHasta(lis,sublis,i-1)
	else:
		return cantSubHasta(lis,sublis,i-1)

def haySublisEnPosr(lis,sublis,i):
	return todosIgualesEntre(lis,sublis,i,len(sublis)-1)

#indicas si en lis en la posicion pos esta sublista sublis[0:i] 
def todosIgualesEntre(lis,sublis,pos,i):
	if i==0:
		return lis[pos]==sublis[0]
	else:
		return todosIgualesEntre(lis,sublis,pos,i-1) and lis[pos+i]==sublis[i] 

c= "¡Vienen los zombies!, no quiero que un zombie se coma mi brazo, porque sino me volvere un zombie que come otro brazo"
resultado= cantSub(c,"zombie")
print(resultado)		

dr= "nananananan"
resr= cantSub(d,"nana")
print(resr)





#------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
# 2)-----------------------------------------------------------------------------------------------------------
def unirProlijo(lis1,lis2):
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

lis1= [1.2, 1.4, 1.6, 1.8]
lis2= [1.1, 1.5, 1.6, 2.0]
print(unirProlijo(lis1,lis2))
print(unirProlijo(lis2,lis1))


#--------------------------- Version recursiva------------------------------------------------------------------------------
def unirProlijor(lis1,lis2):
	if len(lis1)==0 and len(lis2)==0:
		res= []
	elif len(lis2)==0 or (len(lis1)>0 and lis1[len(lis1)-1]<lis2[len(lis2)-1]):
		res= unirProlijor(lis1[:len(lis1)-1],lis2)
		res.append(lis1[len(lis1)-1])
	else:
		res= unirProlijor(lis1,lis2[:len(lis2)-1])
		res.append(lis2[len(lis2)-1])
	return res

print(unirProlijor(lis1,lis2))
print(unirProlijor(lis2,lis1))


