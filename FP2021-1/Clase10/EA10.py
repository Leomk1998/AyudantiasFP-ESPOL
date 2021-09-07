"""
# Examen Final 2016-2 Tema 1: Multas

listaMultas= [(0, 0, 120), (1, 2, 330), (3, 4, 123), (4, 2, 62), (0, 0,50), (4, 4, 89), (0, 3, 25), (2, 0, 43), (3, 2, 21), (0, 0,120)]

import numpy as np
#Literal 1
def generaMatriz(listaMultas):
    matriz = np.zeros((5,5),int)
    for multa in listaMultas:
        x = multa[0]
        y = multa[1]
        matriz[x,y] += multa[2]
        #matriz[x, y] = matriz[x, y] + multa[2]
    return matriz

#print(generaMatriz(listaMultas))
m = generaMatriz(listaMultas)

def sectorTop(matriz):
    norte = np.sum(matriz[0, :])
    sur = np.sum(matriz[4,:])
    oeste = np.sum(matriz[1:4,0])
    este = np.sum(matriz[1:4,4])
    centro = np.sum(matriz[1:4,1:4])
    nombres = np.array(["norte","sur","centro","este","oeste"])
    totalMulta = np.array([norte,sur,centro,este,oeste])
    ind = np.argmax(totalMulta)
    return nombres[ind],totalMulta[ind]
print(sectorTop(m))
"""


"""
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8,9}
C = {5, 4, 7, 0, 1}
Y = {len(A),len(B),len(C)}

X = A | B
E = X - C
print(A.issubset(E))

Y = A & Y
Z = Y - C
print(Z)
"""



import numpy as np

meses = ["ENE","FEB","MAR","ABR","MAY","JUN","AGO","SEP","OCT","NOV","DIC"]

def crearMatriz(nomArchivo):
    archivo = open(nomArchivo,"r")
    etiquetas = archivo.readline().replace("\n","").split(",")
    #print(etiquetas)
    matriz = np.zeros((len(etiquetas),len(meses)),int)
    archivo.readline()
    datos = archivo.readlines()
    for linea in datos:
        listaLinea = linea.replace("\n","").split(",")
        nfila = etiquetas.index(listaLinea[0])
        ncolum = meses.index(listaLinea[1].split("-")[1])
        dato = int(listaLinea[2])
        matriz[nfila,ncolum] += dato
    #print(matriz)
    return np.array(etiquetas),matriz
etiquetas, matriz = crearMatriz("cosechas.txt")


def mesMasRetable(M):
    suma_mes = M.sum(axis=0)
    ind = np.argmax(suma_mes)
    mes = meses[ind]
    maxi = suma_mes[ind]
    return mes,maxi
#print(mesMasRetable(matriz))


def altoBajos(M,k):
    mejorCosechaMes = mesMasRetable(M)[1]
    suma_mes = M.sum(axis=0)
    filtro = suma_mes >= mejorCosechaMes-k
    mesesArreglo = np.array(meses)
    return mesesArreglo[filtro]
#print(altoBajos(matriz,50))
#print(matriz)

def mejorTrimestre(M, Cod, codigo):
    tt = ("T1","T2","T3","T4")
    indFila = list(codigo).index(Cod)
    arreglo = M[indFila,:]
    trimestres = np.zeros(4,int)
    trimestres[0] = np.sum(arreglo[0:3])
    trimestres[1] = np.sum(arreglo[3:6])
    trimestres[2] = np.sum(arreglo[6:9])
    trimestres[3] = np.sum(arreglo[9:12])
    ind = np.argmax(trimestres)
    trimes = tt[ind]
    valor = trimestres[ind]
    return trimes,valor
#print(mejorTrimestre(matriz,"432198",etiquetas))
#print(matriz)

def mejoresNProductos(M, Cod, n):
    suma_productos = M.sum(axis=1)
    orden = np.argsort(suma_productos)[::-1][:n]
    return Cod[orden]
#print(mejoresNProductos(matriz,etiquetas,3))
#print(matriz.sum(axis=1))
#print(etiquetas)


def promedioProductos(M, Cod, codigos):
    vectorTotalProductos = M.sum(axis=1)
    listaIndices = []
    #print(vectorTotalProductos)
    for codigo in codigos:
        listaIndices.append(list(Cod).index(codigo))
    total = 0
    for indice in listaIndices:
        total += vectorTotalProductos[indice]
    promedio = total/len(codigos)
    return promedio
#print(promedioProductos(matriz,etiquetas,["100034","100021"]))
#print(etiquetas)

categorias = {'legumbres':[100034,432198],
'verduras':[100021,100312]}

def porCategoria(M, Cod, categorias):
    for categoria in categorias:
        archivo = open(categoria+".txt","w")
        archivo.write("codigo,ENE,FEB,MAR,ABR,MAY,JUN,JUL,AGO,SEP,OCT,NOV,DIC\n")
        for codigo in categorias[categoria]:
            lista = list(M[list(Cod).index(str(codigo))])
            for i in range(len(lista)):
                lista[i] = str(lista[i])
            archivo.write(str(codigo)+","+",".join(lista)+"\n")
        archivo.close()
print(matriz)
porCategoria(matriz,etiquetas,categorias)






"""
etiquetas.sum(axis=0)
np.sum(etiquetas,axis=0)
"""
"""
dic= {"chofer1":{
        "ene":{
           "KM":1312,
            "LbTotales":1324,
            "barrios": {"barrio1","barrio2"}
        },
        "feb": {
            "KM": 1312,
            "LbTotales": 1324,
            "barrios": {"barrio1", "barrio2"}
        },
        "mar":{
           "KM":1312,
            "LbTotales":1324,
            "barrios": {"barrio1","barrio2"}
        }
    },
    "chofer2":{
        "ene":{
           "KM":1312,
            "LbTotales":1324,
            "barrios": {"barrio1","barrio2"}
        },
        "feb": {
            "KM": 1312,
            "LbTotales": 1324,
            "barrios": {"barrio1", "barrio2"}
        },
        "mar":{
           "KM":1312,
            "LbTotales":1324,
            "barrios": {"barrio1","barrio2"}
        }
    }
}

def Los7Barrios(listaConductores, mes):
    listaBarrios = [] # [barrio1,barrio2...]
    visitasBarrios = [] # [1,2,]
    for conductor in listaConductores:
        dict = cargarDatos(conductor)
        barrios = dict[mes]["barrios"]
        for barrio in barrios:
            if(barrio in listaBarrios):
                ind = listaBarrios.index(barrio)
                visitasBarrios[ind] +=1
            else:
                listaBarrios.append(barrio)
                visitasBarrios.append(1)
    vbarrios = np.array(listaBarrios)
    vvisitas = np.array(visitasBarrios)
    orden = np.argsort(vvisitas)[::-1][:7]
    return list(vbarrios[orden])


dict = {"barrio2":1,
}
visitas = list(dict.values())
barrios = list(dict.keys())



listaBarrios = []
while len(listaBarrios)<7:
    max = 0
    barrio = ""
    for key in dict:
        if(dict[key]>max):
            max = dict[key]
            barrio = key
    dict.pop(key)
    listaBarrios.append(barrio)
"""















"""
import numpy as np
costa = ['Guayaquil','Portoviejo','Manta','Machala']
sierra = ['Quito','Ambato', 'Cuenca','Sto Domingo']
oriente = ['Macas','Tena', 'El Puyo','Zamora']
años = [1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009]
M=np.random.randint(10,1000,size=(len(costa)+len(sierra)+len(oriente),len(años)*2))
"""










