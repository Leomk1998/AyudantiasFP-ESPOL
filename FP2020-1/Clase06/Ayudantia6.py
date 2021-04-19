#Ayudantias 6
#Leonardo Mendoza
#25/Jul/2020

# Examen Parcial 2017-1 Tema 2: YouTubers

import numpy as np

españa = ["elrubiusOMG", "VEGETTA777","Pablo Alborán"]
ecuador = ["enchufetvLIVE", "Kreizivoy","Ecuavisa" ]
mexico = ["Yuya", "Werevertumorro", "CaELiKe" ]

M=np.random.randint(500,5000000,size=(4,len(españa)+len(ecuador)+len(mexico)))

#Literal
#print(M)

rentabilidad = M[3,:]/M[0,:]
#print(españa+ecuador+mexico)
#print(rentabilidad)

renta_es=rentabilidad[:len(españa)]
renta_ec=rentabilidad[len(españa):len(ecuador)+len(españa)]
renta_mex=rentabilidad[len(ecuador)+len(españa):len(ecuador)+len(españa)+len(mexico)]

ind_es=np.argmax(renta_es)
ind_ec=np.argmax(renta_ec)
ind_mx=np.argmax(renta_mex)

listLiteral1=[españa[ind_es],ecuador[ind_ec],mexico[ind_mx]]

#print(listLiteral1)

#Literal2

ind_todos=np.argmax(rentabilidad)
youtubers=ecuador+españa+mexico
literal2=youtubers[ind_todos]

#print(literal2)

#Literal 3

#Cuántos youtubers de España tienen más suscriptores que el youtuber más popular de América(Ecuador y México). Tipo de dato de respuesta: valor entero

popularidad = M[0,:]
maxPopularidadAmerica=np.max(popularidad[len(españa):])
#print(maxPopularidadAmerica)
filtro=popularidad[:len(españa)]>maxPopularidadAmerica
#print(filtro)
matrixMasSubsQueAmerica=popularidad[:len(españa)][filtro]
literal3=matrixMasSubsQueAmerica.shape[0]
#print(literal3)

#Literal 4

filtro=M[0,:]>1000000

#Pregunta
#filtro=nombres=="sony" || nombres=="nintendo"
#a=nombres[filtro]
#filtro=nombres=="nintendo"
#b=nombres[filtro]
#a.extends(b)


#print(filtro)
matrixReproMayorA1M=M[1,:][filtro]
#print(matrixReproMayorA1M)
promedio = np.mean(matrixReproMayorA1M)
#print(promedio) #Respuesta literal 4

#Literal 5

#print(renta_ec)
filtro1 = renta_ec<0.3
filtro2 = np.logical_and(renta_ec>0.31,renta_ec<0.60) #& np.logical_and
filtro3 = renta_ec>0.61
nCategoria1 = renta_ec[filtro1].shape[0]
nCategoria2 = renta_ec[filtro2].shape[0]
nCategoria3 = renta_ec[filtro3].shape[0]
#print(nCategoria1)
arreglo = np.array([[1,2,3],[nCategoria1,nCategoria2,nCategoria3]])
#print(arreglo)

#Literal 6
ganancias_es=np.sum(M[3,:len(españa)])
ganancias_ec=np.sum(M[3,len(españa):len(ecuador)+len(españa)])
ganancias_mex=np.sum(M[3,len(ecuador)+len(españa):len(ecuador)+len(españa)+len(mexico)])

paises=["Espana","Ecuador","Mexico"]
listaGanancias = [ganancias_es,ganancias_ec,ganancias_mex]
ind_max=listaGanancias.index(max(listaGanancias))
ind_min=listaGanancias.index(min(listaGanancias))

porcentaje=((listaGanancias[ind_max]-listaGanancias[ind_min])/listaGanancias[ind_min])*100
print(porcentaje)
print("El pais %s genero %.2f%s mas ganancias que el pais %s"%(paises[ind_min],porcentaje,"%",paises[ind_max]))

# Examen Final 2016-2 Tema 1: Multas

#import numpy as np

M=np.random.randint(500,5000000,size=(4,10))
print(M)
print(M[0])

listaMultas= [[0, 0, 120], [1, 2, 330], [3, 4, 123], [4, 2, 62], [0, 0,50], [4, 4, 89], [0, 3, 25], [2, 0, 43], [3, 2, 21], [0, 0,120]]

#Literal 1

def generarMatriz(listaMultas):
    matrix=np.zeros((5,5),int)
    for multa in listaMultas:
        x=multa[0]
        y=multa[1]
        valor=multa[2]
        matrix[x,y]+=valor
    return matrix
matrix = generarMatriz(listaMultas)
print(matrix)

#Literal 2

def sectorTop(matriz):
    norte = np.sum(matriz[0,:])
    sur = np.sum(matriz[4, :])
    este = np.sum(matriz[1:4,0])
    oeste = np.sum(matriz[1:4,4])
    centro= np.sum(matriz[1:4,1:4])

    '''alternativa
    norte = np.sum(matriz[0,:])
    sur = np.sum(matriz[-1, :])
    este = np.sum(matriz[1:-1,0])
    oeste = np.sum(matriz[1:-1,-1])
    centro= np.sum(matriz[1:-1,1:-1])
    '''

    listaSectores=["Norte","Sur","Este","Oeste","Centro"]
    listaTotales=[norte,sur,este,oeste,centro]
    indMax=listaTotales.index(max(listaTotales))
    sectorMaximo=listaSectores[indMax]
    valor= listaTotales[indMax]
    return (sectorMaximo,valor)

print(sectorTop(matrix))

#np.array() #a*b caracter por caracter
#np.matrix() #m*n con reglas de matrices algebraicas