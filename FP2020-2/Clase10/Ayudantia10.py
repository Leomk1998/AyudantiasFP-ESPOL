#Ayudantias 08/01/2021

# Ejercicio 1
"""
def primerNombre():
    return ("Leonardo",)
print(primerNombre())
print(type(primerNombre()))
"""
# Ejercicio 2
"""
from datetime import datetime
def fecha():
    ahora = datetime.now()
    return ahora.day,ahora.month,ahora.year,ahora.hour,ahora.minute,ahora.second
print(fecha())
print(type(fecha()))
"""
# Ejercicio 3
"""
archivoAlgebra = open("algebra.txt","r")
cedulasAlgebra = archivoAlgebra.readlines()
for i in range(len(cedulasAlgebra)-1):
    cedulasAlgebra[i]=cedulasAlgebra[i][:-1]
archivoCalculo = open("calculo.txt","r")
cedulasCalculo = archivoCalculo.readlines()
for i in range(len(cedulasCalculo)-1):
    cedulasCalculo[i]=cedulasCalculo[i][:-1]
conjuntoCalculo = set(cedulasCalculo)
conjuntoAlgebra = set(cedulasAlgebra)
print(conjuntoCalculo)
print(conjuntoAlgebra)
archivoCalculo.close()
archivoAlgebra.close()

literalA = conjuntoAlgebra.intersection(conjuntoCalculo)
print(literalA)

literalB = conjuntoCalculo.difference(conjuntoAlgebra)
print(literalB)

literalC = conjuntoAlgebra.symmetric_difference(conjuntoCalculo)
print(literalC)

literalD = open("literalD.txt","w")
union = conjuntoCalculo.union(conjuntoAlgebra)
for elem in union:
    literalD.write(elem+"\n")
literalD.close()
"""
# Ejercicio 4
"""
segundosUsuario = int(input("Ingrese una cantidad de segundos: "))
diccionario = {"horas":segundosUsuario//3600,"minutos":(segundosUsuario%3600)//60,"segundos":segundosUsuario%60}
diccionario1 = {} # Para conjuntos set()
diccionario1["horas"]=segundosUsuario//3600
print(diccionario)
print(diccionario1)
"""
# Ejercicio 5
# { "Ecuador" : ("Gye","Quito"...)
# }
archivoCiudades = open("south-america-cities.csv","r",encoding="UTF-8")
leido = archivoCiudades.readline()
diccionarioPaisesSA = {}
leido = archivoCiudades.readlines()
archivoCiudades.close()
paisActual = ""
for linea in leido:
    listaLinea = linea.replace("\n","").split(",")
    if(listaLinea[1] != paisActual):
        diccionarioPaisesSA[listaLinea[1]]=[]
        diccionarioPaisesSA[listaLinea[1]].append(listaLinea[0])
        paisActual = listaLinea[1]
    else:
        diccionarioPaisesSA[listaLinea[1]].append(listaLinea[0])
#print(diccionarioPaisesSA["Uruguay"])

# Ejercicio 6

import random
def ciudadAleatoriaDeUnPais(pais,diccionario):
    ciudadAleatoria = random.choice(diccionario[pais])
    return ciudadAleatoria
#print(ciudadAleatoriaDeUnPais("Ecuador",diccionarioPaisesSA))

# Ejercicio 7
def ciudadAletoriaPaisAleatorio(diccionario):
    paisAleatorio = random.choice(list(diccionario.keys()))
    ciudadAleatoria = ciudadAleatoriaDeUnPais(paisAleatorio,diccionario)
    print(paisAleatorio)
    return ciudadAleatoria
#print(ciudadAletoriaPaisAleatorio(diccionarioPaisesSA))

# Ejercicio 8

def consularPais(diccionario):
    ciudadUsuario = input("Ingrese una ciudad: ").strip().title()
    for pais in diccionario:
        for ciudad in diccionario[pais]:
            if(ciudad==ciudadUsuario):
                return pais
    return "No se ha encontrado esa ciudad"
#print(consularPais(diccionarioPaisesSA))


# Ejercicio 9

def agregarCiudad(ciudad,pais,diccionario):
    diccionario[pais].append(ciudad)
    return "Se ha agregado ciudad exitosamente"
#print(agregarCiudad("Bucay","Ecuador",diccionarioPaisesSA))
#print(consularPais(diccionarioPaisesSA))


# Ejercicio Adicional

archivoCiu = open("south-america-cities.csv","r",encoding="UTF-8")
leido = archivoCiu.readline()
diccionarioPaisesProvincias = {}
leido = archivoCiu.readlines()
archivoCiu.close()
for linea in leido:
    listaLinea = linea.replace("\n","").split(",")
    if(listaLinea[1] not in list(diccionarioPaisesProvincias.keys())):
        diccionarioPaisesProvincias[listaLinea[1]] = {}
        diccionarioPaisesProvincias[listaLinea[1]][listaLinea[2]] = []
        diccionarioPaisesProvincias[listaLinea[1]][listaLinea[2]].append(listaLinea[0])
    else:
        if(listaLinea[2] not in list(diccionarioPaisesProvincias[listaLinea[1]].keys())):
            diccionarioPaisesProvincias[listaLinea[1]][listaLinea[2]] = []
            diccionarioPaisesProvincias[listaLinea[1]][listaLinea[2]].append(listaLinea[0])
        else:
            diccionarioPaisesProvincias[listaLinea[1]][listaLinea[2]].append(listaLinea[0])
#print(diccionarioPaisesProvincias)
print(diccionarioPaisesProvincias["Ecuador"])
print(diccionarioPaisesProvincias["Ecuador"]["Manabí"])