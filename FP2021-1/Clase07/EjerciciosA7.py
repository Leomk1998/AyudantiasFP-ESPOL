def cargarDiccionario(nombreArchivo):
    archivoCiu = open(nombreArchivo,"r",encoding="UTF-8")
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
    return diccionarioPaisesProvincias
def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))


diccionario = cargarDiccionario("south-america-cities.csv")

print(diccionario)
pretty(diccionario)
# diccionario[pais][provincia] = listaDeCiudad


import random


# Ejercicio 1

def ciudadAleatoria(diccionario, pais, provincia):
    if(pais in list(diccionario.keys())):
        if(provincia in list(diccionario[pais].keys())):
            lista = diccionario[pais][provincia]
            return random.choice(lista)
        else:
            return "No existe esa provincia"
    else:
        return "No existe ese país"
print(ciudadAleatoria(diccionario, "Ecuador", "Guayas"))
print(ciudadAleatoria(diccionario, "Ecuador", "Guayanabi"))
print(ciudadAleatoria(diccionario, "Pecuador", "Guayanabi"))


# Ejercicio 2

def provinciaAleatoria(diccionario, pais):
    if(pais in diccionario.keys()):
        lista = list(diccionario[pais].keys())
        return random.choice(lista)
    else:
        return "Ese país no existe"
print(provinciaAleatoria(diccionario, "Ecuador"))
#print(type(list(diccionario.keys())))
#print(type([]))
#print(type((1,2)))


# Ejercicio 3

def paisAleatorio(diccionario):
    lista = list(diccionario.keys())
    return random.choice(lista)
print(paisAleatorio(diccionario))


# Ejercicio 4

def ciudadAleatoriaCualquierProvincia(diccionario,pais):
    pais = pais.title()
    if(pais in diccionario.keys()):
        provincia = random.choice(list(diccionario[pais].keys()))
        ciudad = random.choice(diccionario[pais][provincia])
        return ciudad
    else:
        return "No existe ese país"
print(ciudadAleatoriaCualquierProvincia(diccionario,"ecuador"))


# Ejercicio 5

def ciudadRandom(diccionario):
    pais = random.choice(list(diccionario.keys()))
    provincia = random.choice(list(diccionario[pais].keys()))
    ciudad = random.choice(diccionario[pais][provincia])
    # print(pais,"-"+provincia,"-"+ciudad)
    return ciudad
print(ciudadRandom(diccionario))


# Ejercicio 6

def agregarDato(diccionario):
    pais = input("Ingrese el nombre de un país: ").title().strip()
    provincia = input("Ingrese el nombre de una provincia: ").title().strip()
    ciudad = input("Ingrese el nombre de una ciudad: ").title().strip()
    if(pais in diccionario.keys()):
        if(provincia in diccionario[pais].keys()):
            diccionario[pais][provincia].append(ciudad)
        else:
            diccionario[pais][provincia] = []
            diccionario[pais][provincia].append(ciudad)
    else:
        diccionario[pais] = {}
        diccionario[pais][provincia] = []
        diccionario[pais][provincia].append(ciudad)
    return
agregarDato(diccionario)
agregarDato(diccionario)
agregarDato(diccionario)
pretty(diccionario)
"""
"""
# Ejercicio 7
diccionarioCiudades = {}
for pais in diccionario.keys():
    diccionarioCiudades[pais] = []
    for provincia in diccionario[pais].keys():
        diccionarioCiudades[pais] += (diccionario[pais][provincia])
        #diccionarioCiudades[pais].extend(diccionario[pais][provincia])
pretty(diccionarioCiudades)


# Ejercicio 8

diccionarioAgrupadoPorCiudad = {}
for pais in diccionario.keys():
    for provincia in diccionario[pais].keys():
        for ciudad in diccionario[pais][provincia]:
            diccionarioAgrupadoPorCiudad[ciudad] = { "pais":pais, "provincia":provincia}
#pretty(diccionarioAgrupadoPorCiudad)

def consultarPaisProvincia(diccionario, ciudad):
    if ciudad in diccionario.keys():
        return diccionario[ciudad]["pais"],diccionario[ciudad]["provincia"]
    else:
        return "No existe ciudad"

print(consultarPaisProvincia(diccionarioAgrupadoPorCiudad,"Quito"))



import numpy as np

a = np.array([1,2,3])
print(a)