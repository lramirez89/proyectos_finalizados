def esTriangular(a):
	#tiene que ser creciente o estrictamente creciente?

	#busco el maximo
	i=0
	while i<len(a)-1 and a[i]<=a[i+1]:
		i+=1

	#ahora tiene que ser decreciente
	while i<len(a)-1 and a[i]>=a[i+1]:
		i+=1

	return i==len(a)-1 or len(a)==0

print("esTriangular([2,4,5,7,4,3])",esTriangular([2,4,5,7,4,3]))
print("esTriangular([[2,4,5,7,5,8,4,3,1]])",esTriangular([2,4,5,7,5,8,4,3,1]))
print("esTriangular([])",esTriangular([]))
print("esTriangular([1,2,3,4])",esTriangular([1,2,3,4]))
print("esTriangular([3,2,1])",esTriangular([3,2,1]))