import matplotlib.pyplot as plt

tamanios= [100, 1000, 10000]
tamanios2= [100, 1000, 10000,100000, 1000000]

upSortSlice=[0.0015130043029785156, 0.13906002044677734, 13.66360855102539]
upSortIndex=[0.0018012523651123047, 0.18094873428344727, 18.66147804260254]
bubleSort=[0.00171661376953125, 0.21465468406677246, 23.700605154037476]
mergeSortSlices=[0.0007374286651611328, 0.017360210418701172, 1.936124563217163]
mergeSortIndex=[0.0006744861602783203, 0.017491817474365234, 1.8565523624420166]
mergeSortIndexv2=[0.0004150867462158203, 0.005814552307128906, 0.07195663452148438,0.8997478485107422, 11.15921425819397]
quickSortCopy=[0.0008273124694824219, 0.06575846672058105, 7.520867109298706]
quickSortIndex=[0.0003037452697753906, 0.00458216667175293, 0.11261391639709473,7.703212738037109, 807.7239966392517]
sortNativo=[3.2901763916015625e-05, 0.0003962516784667969, 0.0045757293701171875,0.04860091209411621, 0.4991593360900879]

#fig = plt.figure(figsize=(10,10))
fig, (ax1, ax2) = plt.subplots(1, 2)
#plt.xscale('log')
ax1.plot(tamanios,upSortSlice,label="upSortSlice")
ax1.plot(tamanios,upSortIndex,label="upSortIndex")
ax1.plot(tamanios,bubleSort,label="bubleSort")
ax1.plot(tamanios,mergeSortSlices,label="mergeSortSlices")
ax1.plot(tamanios,mergeSortIndex,label="mergeSortIndex")
ax1.plot(tamanios,quickSortCopy,label="quickSortCopy")
ax1.plot(tamanios2,quickSortIndex,label="quickSortIndex")
ax1.plot(tamanios2,sortNativo,label="sortNativo")
ax1.plot(tamanios2,mergeSortIndexv2,label="mergeSortIndexv2")
ax1.legend(loc='best')

ax2.plot(tamanios,upSortSlice,label="upSortSlice")
ax2.plot(tamanios,upSortIndex,label="upSortIndex")
ax2.plot(tamanios,bubleSort,label="bubleSort")
ax2.plot(tamanios,mergeSortSlices,label="mergeSortSlices")
ax2.plot(tamanios,mergeSortIndex,label="mergeSortIndex")
ax2.plot(tamanios,quickSortCopy,label="quickSortCopy")
ax2.plot(tamanios,quickSortIndex[:3],label="quickSortIndex")
ax2.plot(tamanios,sortNativo[:3],label="sortNativo")
ax2.plot(tamanios,mergeSortIndexv2[:3],label="mergeSortIndexv2")
ax2.legend(loc='best')

#fig.legend(loc='best')
plt.show()