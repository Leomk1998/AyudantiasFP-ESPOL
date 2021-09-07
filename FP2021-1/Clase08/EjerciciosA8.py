'''
#Archivos
Las variables son almacenamiento temporal, es decir, una vez que apagamos la
computadora, perdemos la información.

open(ruta,modo)

Rutas:
    Absoluta: C:\Python25\Lib\idlelib\path_to_libs
    Relativa: drinks.csv archivos/drinks.csv
Modos:
    “r” – abrir como solo lectura, si no existe da error.
    “w” – abrir solo escritura, si no existe, lo crea.
    “a” – abrir como anexar o agregar.
    “+” – abrir como lectura/escritura: "+r" "+w" "+a"
    "x"

Abrir:
mi archivo = open(ruta,modo) #Abrir el archivo
mi_archivo = open(“archivo1.txt”, “r”) #Abrir el archivo en modo lectura.

Entrada:
leido = mi_archivo.read() #Leerá todo el archivo. El string leído será asignado a la variable leido
leido = mi_archivo.read(n) #Leerá n caractetres del archivo. El string leído será asignado a la variable leido
leido = mi_archivo.readline() #Leerá la primera linea del archivo. El string leído será asignado a la variable leido
leido = mi_archivo.readline(n) #Leerá n caracteres de la primera linea.  El string leído será asignado a la variable leido
leido = mi_archivo.readlines() #Retornara una lista, donde cada elemento de esa lista, es una linea del archivo
leido = mi_archivo.readlines(n) #Retornara una lista, leera donde cada elemento de esa lista

Salida:
write(str) = escribe str en el archivo
writelines(list) = escribe cada elemento de list en

Importante:
mi_archivo.close()
'''

"""
#archivo = open("drinks.csv","r")
#leido = archivo.read()
#leido = archivo.read(300)
#leido = archivo.readline() # "...\n"
#leido = archivo.readline(500)
#leido = archivo.readlines() # retorna una ista
#leido = archivo.readlines(300)

archivo = open("presentacion.txt","w")
#numero = 34.2423423423423423
#retorno = archivo.write("Hola me llamo Leonardo".upper())
#print(retorno)
archivo.writelines(["Leonardo\n","Kevin","Carlos","Diego","William","Selena"])
"""

import numpy as np
"""
#np.array([],type=int)

archivoDrinks = open("string_drinks.txt","r")
leido = archivoDrinks.readlines()
arregloPaises = np.array(leido[0].replace("\n","").split(","))
arregloBeer = np.array(leido[1].replace("\n","").split(","), dtype=int)
arregloWine = np.array(leido[2].replace("\n","").split(","))
print(arregloPaises)
print(arregloBeer)
"""

# Ejercicio 1

archivo = open("drinks.csv","r")
archivo.readline()
paises = []
beer = []
spirit = []
wine = []
total = []
contienente = []
listaLeido = archivo.readlines()
#print(listaLeido)
for linea in listaLeido:
    linea = linea.replace("\n","").split(",")
    paises.append(linea[0])
    beer.append(linea[1])
    spirit.append(linea[2])
    wine.append(linea[3])
    total.append(linea[4])
    contienente.append(linea[5])
paises = np.array(paises)
beer = np.array(beer,dtype=int)
spirit = np.array(spirit, dtype=int)
wine = np.array(wine, dtype=int)
total = np.array(total, dtype=float)
contienente = np.array(contienente)


# Ejercicio 2
"""
print(len(paises))
print(paises.size)
print(paises.shape[0])
contador = 0
for pais in paises:
    contador+=1
print(contador)
"""

# Ejercicio 3

def continentList(contient):
    return list(np.unique(contient))
#print(continentList(contienente))


# Ejercicio 4
"""
lista = [1,2,3]
arreglo = np.array([1,2,3])
print(lista+lista)
print(arreglo+arreglo+arreglo)

paisUsuario = input("Ingrese un país:").title()
filtro = paises==paisUsuario
print(filtro)
print(paises[filtro])
print(beer[filtro])
print(spirit[filtro])
print(wine[filtro])
print(total[filtro])
print(contienente[filtro])
"""

# Ejercicio 5
"""
def comprarPaises(pais1,pais2):
    filtro1 = paises == pais1.title()
    filtro2 = paises == pais2.title()
    print("Paises:",paises[filtro1][0],"vs",paises[filtro2][0])
    print("Beer:",beer[filtro1],"vs",beer[filtro2])
    print("Wine:",wine[filtro1],"vs",wine[filtro2])
    print("Total:",total[filtro1][0],"vs",total[filtro2][0])
    print("Cont:",contienente[filtro1],"vs",contienente[filtro2])
    return
comprarPaises("Ecuador","Colombia")
"""

# Ejercicio 6
"""
indiceDelMaximo = np.argmax(total)
#indiceDelMaximo = np.argmax(beer)
#indiceDelMaximo = np.argmax(wine)
valor = np.max(total)
print(paises[indiceDelMaximo],valor)
# Lo mismo con argmin y min
"""

# Ejercicio 7
"""
#np.sort(total)
#orden = np.argsort(total)
#print(paises[orden])
def top10MasAlcohol(total,paises):
    orden = np.argsort(total)
    #orden = paises[-10:]
    #return paises[orden][-10:]
    return paises[orden][::-1][:10]
    return paises[orden][-10:][::-1]
print(top10MasAlcohol(total,paises))
"""
# Ejercicio 8
"""
filtro = total == 0
print(paises[filtro])
#print(contienente[filtro])
"""
# Ejercicio 9
"""
filtro = beer > wine # [5,2,10] > [1,3,11] = [True, False, False]
# filtro = beer < <= > >= == != wine
p = paises[filtro]
b = beer[filtro]
w = wine[filtro]
#print(p)
for i in range(len(p)):
    print(p[i]+":",b[i],w[i])
"""
# Ejercicio 10
"""
filtro = spirit>200
print(paises[filtro])
"""
# Ejercicio 11
"""
# filtro = total >= 10 & total<=12
filtro = np.logical_and(total >= 10,total<=12)
p10l = paises[filtro]
a10l = total[filtro]
print(p10l)
print(a10l)
"""

#Ejercicio 12
"""
contienentesUnicos = continentList(contienente)
for cont in contienentesUnicos:
    filtro = cont == contienente
    paisesDeContinente = paises[filtro]
    alchoholDeContinente = total[filtro]
    if(alchoholDeContinente>0).all():
        print(cont)
        print(paisesDeContinente)
"""
#Ejercicio 13
"""
def consumosContienentes(continentes, continent, total):
    retorno = {}
    for cont in continentes:
        filtro = continent == cont
        retorno[cont] = np.sum(total[filtro])
        # retorno[cont] = np.mean(total[filtro])
    return retorno
contienentesUnicos = continentList(contienente)
print(consumosContienentes(contienentesUnicos,contienente,total))
"""
#Ejercicio 14
"""
def consumosContienentes(continentes, continent, total):
    retorno = {}
    for cont in continentes:
        filtro = continent == cont
        #retorno[cont] = np.sum(total[filtro])
        retorno[cont] = np.mean(total[filtro])
    return retorno
contienentesUnicos = continentList(contienente)
print(consumosContienentes(contienentesUnicos,contienente,total))
"""