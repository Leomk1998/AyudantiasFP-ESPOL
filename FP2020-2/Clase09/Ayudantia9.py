#Ayudantias 9: 18/12/2020
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
    “+” – abrir como lectura/escritura: "+r" "+w" "+a" "r+w"
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


#mi_archivo =open("C:/Users/Leonardo/Desktop/FP2020-2/Ejercicios/Ayudantia9/presentacion.txt","r")
#mi_archivo = open("presentacion.txt","r")
#mi_archivo = open("presentacion.txt","w")
"""
datosLeidos = mi_archivo.read()
#datosLeidos = mi_archivo.read(20)
print(datosLeidos)
"""
"""
datosLeidos = mi_archivo.readline().replace("\n","")
print(datosLeidos)
datosLeidos = mi_archivo.readline(100).replace("\n","")
print(datosLeidos)
datosLeidos = mi_archivo.readline().replace("\n","")
print(datosLeidos)
"""
"""
datos = mi_archivo.readlines()
print(datos)
"""
"""
ncaracteresEscrits= mi_archivo.write("Hola me gusta jugar futbol\nMe gusta leer\n")
mi_archivo.write("Antes escribi: %d caracteres"%ncaracteresEscrits)
"""
"""
mi_archivo.writelines(["Hola\n","Hola\n","Hola\n","Hola\n"])
"""


"""
import numpy as np
miArchivo = open("drinks.csv","r")
cabecera = miArchivo.readline().replace("\n","").split(",")
print(cabecera)
paises = []
beer = []
wine = []
spirit = []
totalLitros = []
contienente = []
datosLeidos = miArchivo.readlines()
print(len(datosLeidos))
for linea in datosLeidos:
    linea_limpia = linea.strip().replace("\n","").split(",")
    paises.append(linea_limpia[0])
    beer.append(int(linea_limpia[1]))
    spirit.append(int(linea_limpia[2]))
    wine.append(int(linea_limpia[3]))
    totalLitros.append(float(linea_limpia[4]))
    contienente.append(linea_limpia[5])

print(paises)
arreglo_paises = np.array(paises)
arreglo_beer = np.array(beer)
print(arreglo_paises)
print(arreglo_beer)
"""

import numpy as np

archivo = open("spotify_ecuador.csv","r")
archivo.readline()
datosLeidos = archivo.readlines()
puesto = []
canciones = []
artista = []
reproducciones = []
url = []
fecha = []
for linea in datosLeidos:
    lineaLimpia = linea.replace("\n","").strip().split(",")
    puesto.append(lineaLimpia[0])
    canciones.append(lineaLimpia[1])
    artista.append(lineaLimpia[2])
    reproducciones.append((lineaLimpia[3]))
    url.append(lineaLimpia[4])
    fecha.append(lineaLimpia[5])
archivo.close()
arreglo_puesto = np.array(puesto)
arreglo_cancion = np.array(canciones)
arreglo_artista = np.array(artista)
arreglo_reproducciones = np.array(reproducciones)
arreglo_url = np.array(url)
arreglo_fecha = np.array(fecha)
#print(arreglo_cancion)


def cancionMasSonada():
    cancionMasSonada = ""
    numeroDeApariciones = 0
    for cancion in np.unique(arreglo_cancion): #[cancion1,cancion2,...,cancionN]
        aparaciones = canciones.count(cancion)
        if(numeroDeApariciones<aparaciones):
            cancionMasSonada = cancion
            numeroDeApariciones = aparaciones
    print("La cancion con mas apariciones es: %s con %s"%(cancionMasSonada,numeroDeApariciones))
#cancionMasSonada()

def artistaMasSonado():
    artistaMasSonado = ""
    numeroDeApariciones = 0
    for artist in np.unique(arreglo_artista):  # [cancion1,cancion2,...,cancionN]
        aparaciones = artista.count(artist)
        if (numeroDeApariciones < aparaciones):
            artistaMasSonado = artist
            numeroDeApariciones = aparaciones
    print("La cancion con mas apariciones es: %s con %s" % (artistaMasSonado, numeroDeApariciones))
#artistaMasSonado()


def consultarArtistaMasSonadoEnUnaFecha():
    fechaUsuario = input("Ingrese la fecha a consultar (YYYY-MM-DD): ").strip()
    filtro = arreglo_fecha==fechaUsuario
    artistaFecha = arreglo_artista[filtro]
    aparicionesMax = 0
    artistaMasSonado =""
    for artista in np.unique(artistaFecha):
        apariciones = list(artistaFecha).count(artista)
        if(aparicionesMax<apariciones):
            aparicionesMax=apariciones
            artistaMasSonado=artista
    print("El artista mas sonado de %s es %s con %s apariciones"%(fechaUsuario,artistaMasSonado,aparicionesMax))
#consultarArtistaMasSonadoEnUnaFecha()

def consultarArtistaMasSonadoEnUnaFecha():
    fechaUsuario = input("Ingrese la fecha a consultar (YYYY-MM-DD): ").strip()
    filtro = arreglo_fecha==fechaUsuario
    artistaFecha = arreglo_artista[filtro]
    aparicionesMax = 0
    artistaMasSonado =""
    for artista in np.unique(artistaFecha):
        apariciones = list(artistaFecha).count(artista)
        if(aparicionesMax<apariciones):
            aparicionesMax=apariciones
            artistaMasSonado=artista
    print("El artista mas sonado de %s es %s con %s apariciones"%(fechaUsuario,artistaMasSonado,aparicionesMax))
#consultarArtistaMasSonadoEnUnaFecha()

def consultarCancionMasSonadoEnUnaFecha():
    fechaUsuario = input("Ingrese la fecha a consultar (YYYY-MM-DD): ").strip()
    filtro = arreglo_fecha==fechaUsuario
    cancionFecha = arreglo_cancion[filtro]
    artistaFecha = arreglo_artista[filtro]
    urlFecha = arreglo_url[filtro]
    reproduccionesFecha = arreglo_reproducciones[filtro]
    print(cancionFecha[0],artistaFecha[0],urlFecha[0],reproduccionesFecha[0])
consultarCancionMasSonadoEnUnaFecha()