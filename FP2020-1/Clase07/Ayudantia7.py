#Ayudantias 7: 1/08/2020
#Leonardo Mendoza

'''
#Archivos
Las variables son almacenamiento temporal, es decir, una vez que apagamos la
computadora, perdemos la información.

open(ruta,modo)

Rutas:
    Absoluta: C:\Python25\Lib\idlelib\path_to_libs
    Relativa: presentacion.txt ../drinks.csv
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





#RutaAbsoluta
'''
mi_archivo = open("C:/Users/Leonardo/Desktop/AyudantiasFP/AyudantiasFP_2020-1/Ejercicios/Ayudantia7/presentacion.txt","r")
leido = mi_archivo.read()
print(leido)
'''

#mi_archivo = open("presentacion.txt", "r") #Abrir el archivo en modo lectura.

#leido = mi_archivo.read()
'''
leido = mi_archivo.read(30)
print("Primer read")
print(leido)
leido = mi_archivo.read(30)
print("Segundo read")
print(leido)
'''

'''
linea1 = mi_archivo.readline() #\n
print("Primer readline")
print(linea1)
linea2 = mi_archivo.readline() #\n
print("Segundo readline")
print(linea2)
'''

'''
leido = mi_archivo.readline(30).replace("\n","")
lista = []
lista.append(leido)
print(lista)
'''

'''
leido = mi_archivo.readlines() # [linea1,linea2,...,linean]
for i in range(len(leido)):
    leido[i]=leido[i].replace("\n","")
print(leido)
'''

'''
leido = mi_archivo.read(30)
print(leido)
mi_archivo.seek(0)
leido = mi_archivo.read(30)
print(leido)
'''

'''
leido = mi_archivo.readlines(30)
print(leido)
'''

#seek(n) Establece el cursor


'''
mi_archivo = open("presentacion1.txt", "w") #Abrir el archivo en modo lectura.
carateresEscritos = mi_archivo.write("Hola me llamo Leonardo \n")

mi_archivo.write("Se han escrito: %d\n"%carateresEscritos)
mi_archivo.write("Se han escrito: {}\n".format(carateresEscritos))
#mi_archivo = open("presentacion.txt", "a") #Abrir el archivo en modo lectura.
mi_archivo.writelines(["Me gusta el futbol\n","Estudio computacion\n"])
entrada = input("Ingresa lo que quieras escribir en el archivo: ")
mi_archivo.write(entrada)
mi_archivo.close()
'''

'''
#mi_archivo = open("presentacion.txt", "a") #Abrir el archivo en modo lectura.
mi_archivo.writelines(["Me gusta el futbol\n","Estudio computacion"])
'''

'''
mi_archivo = open("presentacion1.txt", "r") #Abrir el archivo en modo lectura.
leido = mi_archivo.read()
mi_archivo.write("hola")
'''

'''
mi_archivo = open("presentacion1.txt", "r+") #Abrir el archivo en modo lectura.
leido = mi_archivo.read()
mi_archivo.write(leido)
'''

'''
mi_archivo = open("presentacion1.txt", "a+") #Abrir el archivo en modo lectura.
leido = mi_archivo.read()
mi_archivo.write(leido)
'''

'''
mi_archivo = open("presentacion1.txt", "w+") #Abrir el archivo en modo lectura.
leido = mi_archivo.read()
mi_archivo.write(leido)
'''


#Ejercicio: Leer y guardar en arreglos el archivo string_drinks
'''
import numpy as np

archivo_datos_alcohol = open("string_drinks.txt","r")
paises = archivo_datos_alcohol.readline().strip().replace("\n","")
beer_servings = archivo_datos_alcohol.readline().strip().replace("\n","")
sprint_servings = archivo_datos_alcohol.readline().strip().replace("\n","")
wine_sevings = archivo_datos_alcohol.readline().strip().replace("\n","")
continente = archivo_datos_alcohol.readline().strip().replace("\n","")


apaises = np.array(paises.split(","))
abeer_servings = np.array(beer_servings.split(","),int)
print(abeer_servings)
'''

#Ejercicio: Leer y guardar en arreglos el archivo drinks.csv
'''
archivo_datos_alcohol = open("drinks.csv","r")
paises = ""
beer_servings = ""
sprint_servings = ""
wine_sevings = ""
continente = ""
cabecera = archivo_datos_alcohol.readline()
leido = archivo_datos_alcohol.readlines()

'''

#Primero Forma de solucionar la coma de mas
'''
for i in range(len(leido)):
    if(i==len(leido)-1):
        linea_limpia=leido[i].strip().replace("\n","")
        listaLinea = linea_limpia.split(",")
        paises += listaLinea[0]
        beer_servings += listaLinea[1]
        sprint_servings += listaLinea[2]
        wine_sevings += listaLinea[3]
        continente += listaLinea[4]
    else:
        linea_limpia=leido[i].strip().replace("\n","")
        listaLinea = linea_limpia.split(",")
        paises += listaLinea[0]+","
        beer_servings += listaLinea[1]+","
        sprint_servings += listaLinea[2]+","
        wine_sevings += listaLinea[3]+","
        continente += listaLinea[4]+","
'''

'''
#Segunda solucion (alternativa)
for i in range(len(leido)):
    linea_limpia=leido[i].strip().replace("\n","")
    listaLinea = linea_limpia.split(",")
    paises += listaLinea[0] + ","
    beer_servings += listaLinea[1] + ","
    sprint_servings += listaLinea[2] + ","
    wine_sevings += listaLinea[3] + ","
    continente += listaLinea[4] + ","
paises = paises[0:len(paises)-1]
beer_servings = beer_servings[0:len(beer_servings)-1]
#repetir con todas variables
print(paises)
print(sprint_servings)
print(continente)
'''

#Ejercicio: Leer archivo string_drinks.txt y hacer un archivo
#drinksMejorado.csv agregrando una columna total_servings, la
#cual es

import numpy as np

archivo_datos_alcohol = open("string_drinks.txt","r")
paises = archivo_datos_alcohol.readline().strip().replace("\n","")
beer_servings = archivo_datos_alcohol.readline().strip().replace("\n","")
sprint_servings = archivo_datos_alcohol.readline().strip().replace("\n","")
wine_sevings = archivo_datos_alcohol.readline().strip().replace("\n","")
litros_totales = archivo_datos_alcohol.readline().strip().replace("\n","")
continente = archivo_datos_alcohol.readline().strip().replace("\n","")


apaises = np.array(paises.split(","))
abeer_servings = np.array(beer_servings.split(","),int)
asprint_servings = np.array(sprint_servings.split(","),int)
awine_servings = np.array(wine_sevings.split(","),int)
alitros_totales = np.array(litros_totales.split(","),float)
acontinente = np.array(continente.split(","))
atotal_servings = abeer_servings+asprint_servings+awine_servings

archivoNuevo = open("drinksMejorado.csv","w")
archivoNuevo.write("country,beer_servings,spirit_servings,wine_servings,total_litres_of_pure_alcohol,continent,totalporciones\n")
for i in range(len(apaises)):
    archivoNuevo.write(apaises[i]+",")
    archivoNuevo.write(str(abeer_servings[i])+",")
    archivoNuevo.write(str(asprint_servings[i])+",")
    archivoNuevo.write(str(awine_servings[i])+",")
    archivoNuevo.write(str(alitros_totales[i])+",")
    archivoNuevo.write(acontinente[i]+",")
    archivoNuevo.write(str(atotal_servings[i]))
    archivoNuevo.write("\n")
#Revisar Archivo creado