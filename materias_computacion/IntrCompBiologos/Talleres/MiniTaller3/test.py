from mini3 import * 

## test upSortSlice
print("test upSortSlice:")
l=[6,5,4,3]
upSortSlice(l)
print("upSortSlice([6,5,4,3]):",l)
l=[]
upSortSlice(l)
print("upSortSlice([]):",l)
l=[1,2,3]
upSortSlice(l)
print("upSortSlice([1,2,3]):",l)
l=[3,2,1]
upSortSlice(l)
print("upSortSlice([3,2,1]):",l)
print('\n')

## test upSortIndex
print("test upSorIndex:")
l=[6,5,4,3]
upSortIndex(l)
print("upSortIndex([6,5,4,3]):",l)
l=[]
upSortIndex(l)
print("upSortIndex([]):",l)
l=[1,2,3]
upSortIndex(l)
print("upSortIndex([1,2,3]):",l)
print('\n')


##test bubleSort
print("test bubleSort:")
l=[5,6,1,3]
bubleSort(l)
print("bubleSort([5,6,1,3]):",l)
l=[]
bubleSort(l)
print("bubleSort([]):",l)
l=[1,2,3]
bubleSort(l)
print("bubleSort([1,2,3]):",l)
l=[1,2,3,5,4]
bubleSort(l)
print("bubleSort([1,2,3,5,4]):",l)
print('\n')


##test bubleSort leve modificacion:
print("test bubleSort leve modificacion:")
l=[5,6,1,3]
bubleSortl(l)
print("bubleSortl([5,6,1,3]):",l)
l=[]
bubleSortl(l)
print("bubleSortl([]):",l)
l=[1,2,3]
bubleSortl(l)
print("bubleSortl([1,2,3]):",l)
l=[1,2,3,5,4]
bubleSortl(l)
print("bubleSortl([1,2,3,5,4]):",l)
print('\n')


##test mergeSortSlices
print("test mergeSortSlices:")
l=[7,4,0,6,7]
mergeSortSlices(l)
print("mergeSortSlices([7,4,0,6,7]):",l)
l=[]
mergeSortSlices(l)
print("mergeSortSlices([]):",l)
l=[1,2,3,4]
mergeSortSlices(l)
print("mergeSortSlices([1,2,3,4]):",l)
l=[5,4,3]
mergeSortSlices(l)
print("mergeSortSlices([5,4,3]):",l)
print("\n")


##test mergeSortIndex
print("test mergeSortIndex")
l=[5,4,3,2]
mergeSortIndex(l)
print("mergeSortIndex([5,4,3,2]:",l)
l=[]
mergeSortIndex(l)
print("mergeSortIndex([]:",l)
l=[1,2,4]
mergeSortIndex(l)
print("mergeSortIndex([1,2,4]:",l)
l=[5,4,5,0]
mergeSortIndex(l)
print("mergeSortIndex([5,4,5,0]:",l)
print('\n')

##test mergeSortIndexv2
print("test mergeSortIndex version 2")
l=[5,4,3,2]
mergeSortIndexv2(l)
print("mergeSortIndex([5,4,3,2]:",l)
l=[]
mergeSortIndexv2(l)
print("mergeSortIndex([]:",l)
l=[1,2,4]
mergeSortIndexv2(l)
print("mergeSortIndex([1,2,4]:",l)
l=[5,4,5,0]
mergeSortIndexv2(l)
print("mergeSortIndex([5,4,5,0]:",l)
print('\n')


##test quickSortCopy
print("test quickSortCopy:")
l=[4,3,2,1]
quickSortCopy(l)
print("quickSortCopy([4,3,2,1]):",l)
l=[4]
quickSortCopy(l)
print("quickSortCopy([4]):",l)
l=[]
quickSortCopy(l)
print("quickSortCopy([]):",l)
l=[5,6,7]
quickSortCopy(l)
print("quickSortCopy([5,6,7]):",l)
l=[5,6,5,1]
quickSortCopy(l)
print("quickSortCopy([5,6,5,1]):",l)
print('\n')


##test quickSortIndex
print("quickSortIndex:")
l=[5,4,3,2,1]
quickSortIndex(l)
print("quickSortIndex([5,4,3,2,1]):",l)
l=[]
quickSortIndex([])
print("quickSortIndex([]):",l)
l=[1,2,3]
quickSortIndex(l)
print("quickSortIndex([1,2,3]):",l)
l=[5,4,1,2,3]
quickSortIndex(l)
print("quickSortIndex([5,4,1,2,3]):",l)
print('\n')

##test quickSortIndexv2
print("quickSortIndex version 2:")
l=[5,4,3,2,1]
quickSortIndex2(l)
print("quickSortIndex2([5,4,3,2,1]):",l)
l=[]
quickSortIndex2([])
print("quickSortIndex2([]):",l)
l=[1,2,3]
quickSortIndex2(l)
print("quickSortIndex2([1,2,3]):",l)
l=[5,4,1,2,3]
quickSortIndex2(l)
print("quickSortIndex2([5,4,1,2,3]):",l)