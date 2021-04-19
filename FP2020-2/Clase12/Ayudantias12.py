#Tema 1

a = {2, 8, 14, 19, 20}
b = {14, 16, 20, 4, 2, 1}
c = a.symmetric_difference(b)
resultado = (a - c).union(b - c)
print(resultado)

#Tema 2

#1
"""
import pandas as pd
df = pd.read_csv("especies.csv")
print(df.to_numpy())
"""
def crearDiccionario(archivo,n):
    dicc = {}
    archivoEspecies = open(archivo,"r")
    paises = archivoEspecies.readline().replace("\n","").split(",")
    lineas = archivoEspecies.readlines()
    for linea in lineas:
        listaEspecie = linea.replace("\n","").split(",")
        dicc[listaEspecie[0]] = []
        for i in range(1,len(listaEspecie)):
            if int(listaEspecie[i])>n:
                dicc[listaEspecie[0]].append((paises[i],int(listaEspecie[i])))
    return dicc
#diccionario = crearDiccionario("especies.csv",100)
#print(diccionario)
#2
def masPopular(dicc,especie):
    paisMaximo = ""
    numeroMaximo = 0
    for i in range(len(dicc[especie])):
        if(dicc[especie][i][1]>numeroMaximo):
            numeroMaximo = dicc[especie][i][1]
            paisMaximo = dicc[especie][i][0]
    return paisMaximo
#print(masPopular(diccionario,"Nepal"))
#3
def paisEspecie(diccionario):
    dicc = {}
    conjuntoPais = set()
    for especie in diccionario:
        for tupla in diccionario[especie]:
            conjuntoPais.add(tupla[0])
    for pais in conjuntoPais:
        dicc[pais] = []
        for especie in diccionario:
            for tupla in diccionario[especie]:
                if(tupla[0]==pais):
                    dicc[pais].append(especie)
    return dicc
#diccionarioPaises = paisEspecie(diccionario)
#print(paisEspecie(diccionario))
#4
def especiesEnComun(diccPais,paises):
    conjunto = set()
    for pais in paises:
        conjunto = conjunto.union(set(diccPais[pais]))
    for pais in paises:
        conjunto = conjunto.intersection(set(diccPais[pais]))
    return tuple(conjunto)
#print(especiesEnComun(diccionarioPaises,["Ecuador","Australia"]))


#Tema 3

import numpy as np
costa = ['Guayaquil','Portoviejo','Manta','Machala']
sierra = ['Quito','Ambato', 'Cuenca','Sto Domingo']
oriente = ['Macas','Tena', 'El Puyo','Zamora']
años = [1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009]
M=np.random.randint(10,1000,size=(len(costa)+len(sierra)+len(oriente),len(años)*2))

#print(M)

#1. Cantidad total de turistas que ingresaron a las ciudades del país en el año 2007. (int)

indice = años.index(2007)*2
v = M[:,indice]
#print(np.sum(v))

#2. La capacidad hotelera promedio para cada una de las ciudades de la sierra considerando todos los años.(vector de float)

MatrizSierra = M[len(costa):len(costa)+len(sierra),:]
listaPromedios = []
for i in range(MatrizSierra.shape[0]):
    lista = []
    for j in range(1,MatrizSierra.shape[1],2):
        lista.append(MatrizSierra[i,j])
    listaPromedios.append(np.mean(np.array(lista)))
#print(np.array(listaPromedios))

#3. El número de años en los que la cantidad de turistas fue mayor que la capacidad hotelera para la ciudad deMachala. (int)

indiceMachala = costa.index("Machala")
vectorMachala = M[indiceMachala,:]
cantidadYears = 0
for i in range(0,len(vectorMachala),2):
    if(vectorMachala[i]>vectorMachala[i+1]):
        cantidadYears+=1
print(cantidadYears)

#4. Los años en la que la capacidad hotelera del país fue superior a 5000. (vector o lista de int)
vectorTotalPais = M.sum(axis=0)
listaAños = []
for i in range(1,len(vectorTotalPais),2):
    if(vectorMachala[i]>5000):
        listaAños.append(años[(i-1)//2])
print(listaAños)


#5

sumaCiudades = M.sum(axis=1)
listaCiudades = costa+sierra+oriente
listaCiudadesTop = []
sumaCiudades = sumaCiudades[0::2]
indicesOrdenados = sumaCiudades.argsort()[::-1][:3]
for indice in indicesOrdenados:
    listaCiudadesTop.append(listaCiudades[indice])
    #print(sumaCiudades[indice])
#print(listaCiudadesTop)

# Tema 4
m=10
n=10
M=np.random.randint(0,100,size=(m,n))
print(M)
#1
def probabilidad_contagio(M, f, c):
    lista=[]
    lista.append(M[f,c+1])
    lista.append(M[f,c-1])
    lista.append(M[f+1,c])
    lista.append(M[f-1,c])
    return np.mean(np.array(lista,float))
#print(probabilidad_contagio(M,5,5))

#2

# B
import random
numeroAleatorio = random.randrange(2,201,2)
print(numeroAleatorio)
# A
while(M[1,1]<20 and M[1,M.shape[0]-1]<20):
    numeroAleatorio = random.randrange(2, 201, 2)
    vacunar(M, M.argmax()//M.shape[1],M.argmax()-((M.argmax()//M.shape[1])*M.shape[1]), numeroAleatorio)