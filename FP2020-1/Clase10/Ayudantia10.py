# Ayudantia: 22-Ago-2020
# Leonardo Mendoza

#Ejercicio 1
#Pida al usuario una cantidad de segundos e imprima un diccionario con las
#horas, minutos y segundos correspondiente a esa cantidad de segundos ingresada.

segundosUsuario = int(input("Ingrese una cantidad de segundos: "))
horas = segundosUsuario//3600
minutos = (segundosUsuario%3600)//60
segundos = (segundosUsuario%60)
diccionario = {"horas":horas,"minutos":minutos,"segundos":segundos}
print(diccionario)

#Ejercicio 2
#Cree una función crearDiccionario() que retorne un diccionario con sus datos,
# el cual contenga las siguientes claves: nombre, apellido, edad, materias
# (una tupla con las materias que está tomando este semestre)
# y notas1P (una tupla con las notas de primer parcial de dichas materias).

def crearDiccionario():
    diccionario = {}
    diccionario["nombre"]="Leonardo"
    diccionario["apellido"]="Mendoza"
    diccionario["edad"]=21
    diccionario["materias"]=("SO","IS","SI","ICD","DP")
    diccionario["notas1P"]=(60,60,40,80,70)
    return diccionario
diccionario = crearDiccionario()

#Ejercicio 3
#Suponga que usted se cambio el nombre y que además necesita sumar un año más a su edad.
# Cree un nuevo diccionario con esas dos claves y actualice el diccionario anterior.

#print(diccionario)
diccionarioActualizado = {"nombre":"Nicolas","edad":diccionario["edad"]+1}
diccionario["apellido"] = "Mendoza Kuffo"
diccionario.update(diccionarioActualizado)
#print(diccionario)

#Ejercicio 4
#Cree una función que reciba como parámetro una materia y un diccionario
# resultante de la función anterior, y que retorne la nota del primer parcial
# de dicha materia o un mensaje de error en caso de que no se encuentre.

def consultarNota(materia,diccionario):
    indice=-1
    for i in range(len(diccionario["materias"])):
        if diccionario["materias"][i]==materia:
            indice=i
    #indice = diccionario["materias"].find(materia)
    if(indice==-1):
        return "No se ha encontrado la materia"
    else:
        return diccionario["notas1P"][indice]

#print(consultarNota("FDP",diccionario))

#Ejercicio 5
#Para un diccionario con el formato de la función crearDiccionario(),
# agregue una nueva clave “recomendaciones”, la cual es una tupla,
# donde si el estudiante tiene una nota menor a 60 se guarde “Hay que mejorar”,
# si tiene una nota entre 60 y 75 “No está mal, pero puede mejorar”
# y si el estudiante tiene una nota mayor a 75 “Sigue así”.


def crearRecomendaciones(diccionario):
    lista = []
    for nota in diccionario["notas1P"]:
        if(nota <60):
            lista.append("Hay que mejorar")
        elif(nota >= 60 and nota <=75 ):
            lista.append("No está mal, pero puede mejorar")
        elif(nota>75):
            lista.append("Sigue así")
        else:
            lista.append("Error: No hay recomendacion")
    tupla = tuple(lista)
    diccionario["recomendaciones"]=tupla
    return diccionario
print(crearRecomendaciones(diccionario))

#Ejercicio 6
#Suponga que usted tiene un archivo con ciudades de Sudamérica, con el siguiente formato:
#name,country,subcountry
#...
#Guayaquil,Ecuador,Guayas
#...
#Cargue dicho archivo en un diccionario, donde las claves sean los países
# y los valores sean una tupla con las ciudades de ese país.

archivosPaises = open("south-america-cities.csv","r",encoding="utf-8") #Encoding porque el archivo tiene caracteres espciales
cabecera = archivosPaises.readline()
leido = archivosPaises.readlines()
#print(leido)
diccionarioPaises = {}
# { "Ecuador" : ("Guayaquil,"Quito"...)
paisInicial=""
for linea in leido:
    listaLinea = linea.split(",")
    if(listaLinea[1] != paisInicial):
        paisInicial = listaLinea[1]
        diccionarioPaises[listaLinea[1]] = []
        diccionarioPaises[listaLinea[1]].append(listaLinea[0])
    else:
        diccionarioPaises[listaLinea[1]].append(listaLinea[0])
#print(diccionarioPaises)
for clave in diccionarioPaises.keys():
    diccionarioPaises[clave] = tuple(diccionarioPaises[clave])
#print(diccionarioPaises)
#print(diccionarioPaises["Ecuador"])
archivosPaises.close()


#Ejercicio 7
#Escriba una función que reciba como parámetro el nombre de un país
# y retorne una ciudad aleatoria de dicho país.

import random
def funcionCiudadAletoriaDeUnPais(pais,diccionario):
    ciudadAletoria = diccionario[pais][random.randint(0,len(diccionario[pais])-1)]
    return ciudadAletoria
#print(funcionCiudadAletoriaDeUnPais("Argentina",diccionarioPaises))

#Ejercicio 8
#Escriba una función que escoja una ciudad aleatoria de un país aleatorio.

def ciudadAleatoriaPaisAleatorio(diccionario):
    #print(list(diccionario.keys()))
    paisAleatorio = list(diccionario.keys())[random.randint(0,len(list(diccionario.keys()))-1)]
    ciudadAletoria = diccionario[paisAleatorio][random.randint(0, len(diccionario[paisAleatorio]) - 1)]
    return paisAleatorio,ciudadAletoria
#print(ciudadAleatoriaPaisAleatorio(diccionarioPaises))

#Ejercicio 9
#Escriba una función que solicite al usuario el nombre de una ciudad
# y retorne el nombre del país al que pertenece esa ciudad.

def consultarCiudad(diccionario):
    ciudadUsuario = input("Ingrese la ciudad que quiere consular: ").strip().title()#.replace("í","i")
    #Santo Domingo De Los Colorados: Llevar los c
    for pais in diccionario:
        for ciudad in diccionario[pais]:
            if ciudad.title()==ciudadUsuario:
                return pais
    return "No se encontro esa ciudad"
#print(consultarCiudad(diccionarioPaises))

#Ejercicio 10
#Escriba una función que reciba como parámetros el nombre de un país
# y el nombre de una ciudad, actualizando el diccionario de tal forma
# que se agregue a la tupla la ciudad ingresada.

def agregarCiudad(pais, ciudad, diccionario):
    lista = list(diccionario[pais])
    lista.append(ciudad)
    diccionario[pais] = tuple(lista)
    return diccionario
#print(agregarCiudad("Ecuador","Madrid",diccionarioPaises))
#print(diccionarioPaises["Ecuador"])

#Ejercicio 11
#A partir del archivo, cree un diccionario con las mismas claves (los países),
# pero esta vez los valores serán diccionarios (anidados)
# con dos claves (ciudades y subpaíses).

#{Ecuador: {subpais:(guayas,manabi...),ciudad:(guayaquil,manta..)}...}
archivosPaises = open("south-america-cities.csv","r",encoding="utf-8")
cabecera = archivosPaises.readline()
leido = archivosPaises.readlines()
#print(leido)
diccionarioPaises = {}
# { "Ecuador" : ("Guayaquil,"Quito"...)
paisInicial=""
for linea in leido:
    listaLinea = linea.split(",")
    if(listaLinea[1] != paisInicial):
        paisInicial = listaLinea[1]
        diccionarioPaises[listaLinea[1]] = {"ciudades":[],"subpais":[]}
        diccionarioPaises[listaLinea[1]]["ciudades"].append(listaLinea[0])
        diccionarioPaises[listaLinea[1]]["subpais"].append(listaLinea[2].replace("\n",""))
    else:
        diccionarioPaises[listaLinea[1]]["ciudades"].append(listaLinea[0])
        diccionarioPaises[listaLinea[1]]["subpais"].append(listaLinea[2].replace("\n",""))
#print(diccionarioPaises)
for clave in diccionarioPaises.keys():
    diccionarioPaises[clave]["ciudades"] = tuple(diccionarioPaises[clave]["ciudades"])
    diccionarioPaises[clave]["subpais"] = tuple(diccionarioPaises[clave]["subpais"])
print(diccionarioPaises)
print(diccionarioPaises["Ecuador"])

#Ejercicio 12
#Escriba una función que reciba una ciudad y que la busque dentro de ecuador,
# retornando la provincia a la que pertenecer esa ciudad.

def consultarProvincia(diccionario): #Adicional: Consultar la provincia de una ciudad de Ecuador
    ciudadUsuario = input("Ingrese el nombre de una ciudad: ").strip().title()
    for i in range(len(diccionario["Ecuador"]["ciudades"])):
        if(diccionario["Ecuador"]["ciudades"][i]==ciudadUsuario):
            return diccionario["Ecuador"]["subpais"][i]
    return "No se encontro la ciudad"

print(consultarProvincia(diccionarioPaises))