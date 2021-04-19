# Ayudantia 12: 05/Sep/2020
# Leonardo Mendoza

#Examen Final 2019 - 2 V1

#Tema 1

a = {2, 8, 14, 19, 20}
b = {14, 16, 20, 4, 2, 1}
c = a.symmetric_difference(b)
resultado = (a - c).union(b - c)
print(resultado)


#TEMA 2


#1
def crear_diccionario(archivo, n):
    dicc = {}
    archivoEspecies = open(archivo,"r")
    paises = archivoEspecies.readline().replace("\n","").split(",")
    especies = archivoEspecies.readlines()
    for linea in especies:
        listaEspecie = linea.replace("\n","").split(",")
        dicc[listaEspecie[0]]=[]
        for i in range(1,len(listaEspecie)):
            if int(listaEspecie[i])>n:
                dicc[listaEspecie[0]].append((paises[i],int(listaEspecie[i])))
    return dicc

dicc = crear_diccionario("especies.csv",100)

#2

def mas_popular(dicEspecie, especie):
    paisMaxima=""
    numeroMaximo=0
    for i in range(len(dicEspecie[especie])):
        if dicEspecie[especie][i][1]>numeroMaximo:
            numeroMaximo=dicEspecie[especie][i][1]
            paisMaxima=dicEspecie[especie][i][0]
    return paisMaxima
#print(mas_popular(dicc,"Tigre de Bengala"))

#3

def pais_especie(dicEspecie):
    dicc={}
    conjuntoPaises = set()
    for value in dicEspecie:
        for tupla in dicEspecie[value]:
            conjuntoPaises.add(tupla[0])
    for pais in conjuntoPaises:
        dicc[pais]=[]
        for value in dicEspecie:
            for tupla in dicEspecie[value]:
                if tupla[0]==pais:
                    dicc[pais].append(value)
    return dicc
diccpais = pais_especie(dicc)
print(diccpais)

#4
def especies_en_comun(dicPais, lista_paises):
    conjunto = set()
    for pais in lista_paises:
        conjunto = conjunto.union(set(dicPais[pais]))
    for pais in lista_paises:
        conjunto = conjunto.intersection(set(dicPais[pais]))
    return conjunto
print(especies_en_comun(diccpais,["Ecuador","Japon","Honduras"]))

#TEMA 3


import numpy as np

costa = ['Guayaquil','Portoviejo','Manta','Machala']
sierra = ['Quito','Ambato', 'Cuenca','Sto Domingo']
oriente = ['Macas','Tena', 'El Puyo','Zamora']
años = [1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009]
M=np.random.randint(10,1000,size=(len(costa)+len(sierra)+len(oriente),len(años)*2))

#print(M)

# 1. Cantidad total de turistas que ingresaron a las ciudades del país en el año 2007. (int)

indice = años.index(2007)*2
v = M[:,indice]
#print(np.sum(v))


#2. La capacidad hotelera promedio para cada una de las ciudades de la sierra considerando todos los años.
#(vector de float)

vectorSierra = M[len(costa):len(costa)+len(sierra),:]
lista = []
listaFinal = []
for i in range(vectorSierra.shape[0]):
    for j in range(1,vectorSierra.shape[1],2):
        lista.append(vectorSierra[i,j])
    listaFinal.append(np.mean(np.array(lista,float)))
arreglo = np.array(listaFinal)
#print(arreglo)

#3 Machala

indiceMachala = costa.index("Machala")
vectorMachala = M[indiceMachala,:]
cantidadYears = 0
for i in range(0,len(vectorMachala),2):
    if(vectorMachala[i]>vectorMachala[i+1]):
        cantidadYears+=1
        #print(años[i//2])
#print(cantidadYears)



#4

sumaTodoElPais = M.sum(axis=0)
listaYears = []
for i in range(1,len(sumaTodoElPais),2):
    if(sumaTodoElPais[i]>5000):
        listaYears.append(años[(i-1)//2])
print(listaYears)


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