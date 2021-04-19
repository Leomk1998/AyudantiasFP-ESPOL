# Fecha: 24/Sep/2020
# Leonardo Mendoza

# Examen Mejoramiento 2019-1

#TEMA 1

#Literal 1
import numpy as np
meses = ["ENE","FEB","MAR","ABR","MAY","JUN","JUL","AGO","SEP","OCT","NOV","DIC"]
def crearMatriz(nomArchivo):
    archivo = open(nomArchivo,"r")
    listaCodigos = archivo.readline().replace("\n","").split(",")
    vectorProductos = np.array(listaCodigos)
    matriz = np.zeros((len(listaCodigos),len(meses)),int)
    cabecera = archivo.readline()
    datos=archivo.readlines()
    for linea in datos:
        listaLinea = linea.replace("\n","").split(",")
        mes = listaLinea[1].split("-")[1]
        matriz[listaCodigos.index(listaLinea[0]),meses.index(mes)] += int(listaLinea[2])
    return vectorProductos,matriz
tuplaResultados = crearMatriz("cosechas.txt")
M = tuplaResultados[1]
VectorCod = tuplaResultados[0]
#print(M)
#print(VectorCod)
#Literal 2
def mesMasRentable(M):
    vectorSumaMeses = M.sum(axis=0)
    indceMesMaximo = np.argmax(vectorSumaMeses)
    return meses[indceMesMaximo], vectorSumaMeses[indceMesMaximo]
#print(mesMasRentable(M))
#Literal 3
def altoBajos(M, k):
    vectorSumaMeses = M.sum(axis=0)
    cosechaMesMasRentable = mesMasRentable(M)[1]
    mesesBajos = []
    for i in range(len(vectorSumaMeses)):
        if vectorSumaMeses[i]>=k and vectorSumaMeses[i]<cosechaMesMasRentable:
            mesesBajos.append(meses[i])
    return tuple(mesesBajos)
#print(altoBajos(M,0))
#Literal 4
def mejorTrimestre(M, Cod, codigo):
    trimestres = ("T1","T2","T3","T4")
    indice = list(Cod).index(codigo)
    vectorCodigo = M[indice]
    sumaTimestre = np.array([np.sum(vectorCodigo[0:3]),np.sum(vectorCodigo[3:6]),
                       np.sum(vectorCodigo[6:9]),np.sum(vectorCodigo[9:12])])
    #print(sumaTimestre)
    return trimestres[np.argmax(sumaTimestre)]
#print(mejorTrimestre(M,VectorCod,"432198"))
#Literal 5
def mejoresNProductos(M, Cod, n):
    vectorSumaProductos = M.sum(axis=1)
    vectorOrdenadoDeMenorAMayor = Cod[np.argsort(vectorSumaProductos)]
    VectorOrdenardo = vectorOrdenadoDeMenorAMayor[::-1]
    masCosechados = VectorOrdenardo[:n]
    return masCosechados
#print(mejoresNProductos(M,VectorCod,2))
#Literal 6
def promedioProductos(M, Cod, codigos):
    vectorSumaProductos = M.sum(axis=1)
    indices = []
    for codigo in codigos:
        indices.append(list(Cod).index(codigo))
    total = 0
    for indice in indices:
        total+=vectorSumaProductos[indice]
    promedio = total/len(codigos)
    return promedio
#print(promedioProductos(M,VectorCod,['432198','100021','100034']))
#Literal 7
categorias = {'legumbres':[100034,100312],
'verduras':[100021,432198]}
def porCategoria(M, Cod, categorias):
    for categoria in categorias:
        archivo = open(categoria+".txt","w")
        archivo.write("codigo,"+",".join(meses)+"\n") #Cabecera
        for codigo in categorias[categoria]:
            lista = list(M[list(Cod).index(str(codigo))])
            for i in range(len(lista)):
                lista[i]=str(lista[i])
            archivo.write(str(codigo)+","+",".join(lista)+"\n")
        archivo.close()
    return
#porCategoria(M,VectorCod,categorias)


#TEMA3

A = 'Num empresas,17,0|9|1,10|19|2,20|29|3'
campos = A.split(',')
valores = []
for rango in campos[2:]:
    valores.append(int(rango.split('|')[0]))
print(valores)

#TEMA2

# C = ['Transportes', 'Alimentos', 'Deportes']
# perteneceCategoria(palabra, categoria)
#puntajes = {'Transportes':{'a':10, 't':4, 'f':5, ...},
#'Deportes': {'a':3, 'z':5, 't':10, ...},
#... }
import random
puntajes=0
for i in range(5):
    categoriaAleatoria = random.choice(c)
    palabraUsuario = input("Ingrese una palabra para la categoria "+categoriaAleatoria+": ")
    if(perteneceCategoria(palabraUsuario, categoriaAleatoria)):
        for letra in string.split(""): #Caballo
            puntaje+=puntajes[categoriaAleatoria][letra]
    else:
        puntaje+=0
if puntajes > 500:
    print("GANO")
else:
    print("perdio")