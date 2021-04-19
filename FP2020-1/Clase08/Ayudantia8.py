import numpy as np

archivo = open("spotify_ecuador.csv","r")
cabecera = archivo.readline().split(",")
#print(cabecera)
datosLeidos=archivo.readlines()
puesto=""
nombreCancion = ""
artista = ""
reproducciones = ""
url=""
fecha=""
for i in range(len(datosLeidos)):
    listaLinea = datosLeidos[i].split(",")
    if i == len(datosLeidos)-1:
        puesto+=listaLinea[0]
        nombreCancion+=listaLinea[1]
        artista+=listaLinea[2]
        reproducciones+=listaLinea[3]
        url+=listaLinea[4]
        fecha+=listaLinea[5]
    else:
        puesto+=listaLinea[0]+","
        nombreCancion += listaLinea[1]+","
        artista += listaLinea[2]+","
        reproducciones += listaLinea[3]+","
        url += listaLinea[4]+","
        fecha += listaLinea[5]+","
archivo.close()

apuestos = np.array(puesto.split(","))
anombres = np.array(nombreCancion.split(","))
aartistias = np.array(artista.split(","))
areproducciones = np.array(reproducciones.split(","))
aurl = np.array(url.split(","))
afecha = np.array(fecha.split(","))
#print(afecha)

def artistaMasSonado():
    cancionMax=""
    aparicionesMax=0
    for cancion in np.unique(anombres):
        aparicionesA = list(anombres).count(cancion)
        if(aparicionesMax<aparicionesA):
            aparicionesMax=aparicionesA
            cancionMax=cancion
    print("Las cancion con mas apariciones es %s con %d"%(cancionMax,aparicionesMax))

def cancionMasSonado():
    cancionMax=""
    aparicionesMax=0
    for cancion in np.unique(anombres):
        aparicionesA = list(anombres).count(cancion)
        if(aparicionesMax<aparicionesA):
            aparicionesMax= aparicionesA
            cancionMax=cancion
    print("La cancion con mas apariciones es %s con %d"%(cancionMax,aparicionesMax))

def consultarArtistaMasSonadoDeUnaFecha():
    #2017 - 01 - 02
    fecha=input("Ingrese una fecha(AAAA-MM-DD): ").strip()+"\n"
    filtro = afecha==fecha
    artistaFiltrado = aartistias[filtro]
    fecha=fecha[0:len(fecha)-1]
    if(len(artistaFiltrado)==0):
        print("No se econtro el artista mas sonado de esa fecha.")
    else:
        print("El artista mas sonado del %s es %s"%(fecha,artistaFiltrado[0]))

def consultarCancionMasSonadoDeUnaFecha():
    #2017 - 01 - 02
    fecha=input("Ingrese una fecha(AAAA-MM-DD): ").strip()+"\n"
    filtro = afecha==fecha
    cancionesFiltradas = anombres[filtro]
    fecha=fecha[0:len(fecha)-1]
    if(len(cancionesFiltradas)==0):
        print("No se econtro la cancion mas sonado de esa fecha.")
    else:
        print("La cancion mas sonada del %s es %s"%(fecha,cancionesFiltradas[0]))

def ConsultarURLdeCancion():
    cancionUser = input("Ingrese el nombre de una cancion: ")
    filtro = anombres==cancionUser
    urlFiltrada = aurl[filtro]
    if(len(urlFiltrada)==0):
        print("No se encontro la url de esa cancion.")
    else:
        print("La URL de %s es %s"%(cancionUser,urlFiltrada[0]))

def ConsultarURLdeCancionAleatoria():
    urlRandom = np.random.choice(aurl)
    print("Cancion aleatoria %s"%(urlRandom))

def ReporteCancionesMasSonadas():
    filtro = apuestos=="1"
    cancionesMasSonadas = np.unique(anombres[filtro])
    artistaCMasSonadas = np.unique(aartistias[filtro])
    archivo = open("reporteDeN1.txt","w")
    archivo.write("Canciones que han estado mas veces en el top1:\n")
    for i in range(len(cancionesMasSonadas)):
        archivo.write("%d. %s\n"%(i+1,cancionesMasSonadas[i]))
    archivo.write("Artistas que han estado mas veces en el top1:\n")
    for i in range(len(artistaCMasSonadas)):
        archivo.write("%d. %s\n" % (i + 1, artistaCMasSonadas[i]))

opcion=""
while opcion != "0":
    print("MENU DATOS DE SPOTIFY ECUADOR")
    print("1. Estadisticas")
    print("2. Consultas")
    print("3. Reportes")
    print("Ingrese 0 para salir.")
    opcion = input("Ingrese una opcion: ").strip()
    if(opcion=="1"):
        print("Menu de Estadisticas")
        print("1. Artista mas sonado")
        print("2. Cancion mas sonada")
        print("Ingrese 'salir' para volver al menu principal")
        opcion1 = input("Ingrese una opcion: ").strip()
        if(opcion1=="1"):
            artistaMasSonado()
        elif opcion1=="2":
            cancionMasSonado()
        elif opcion1=="3":
            print("")
        elif opcion1=="salir":
            continue;
        else:
            print("Opcion Incorrecta")
    elif (opcion == "2"):
        print("Menu de Consultas")
        print("1. Artista mas sonado de una fecha")
        print("2. Cancion mas sonada de una fecha")
        print("3. Url de una cancion")
        print("4. Url de una cancion aleatoria")
        print("Ingrese 'salir' para volver al menu principal")
        opcion1 = input("Ingrese una opcion: ").strip()
        if (opcion1 == "1"):
            consultarArtistaMasSonadoDeUnaFecha()
        elif opcion1 == "2":
            consultarCancionMasSonadoDeUnaFecha()
        elif opcion1 == "3":
            ConsultarURLdeCancion()
        elif opcion1 == "4":
            ConsultarURLdeCancionAleatoria()
        elif opcion1 == "salir":
            continue;
        else:
            print("Opcion Incorrecta")
    elif (opcion == "3"):
        print("Menu de Consultas")
        print("1. Reporte mas sonado")
        print("2. Reporte mix de canciones")
        print("3. Reporte de canciones mas sonadas")
        print("Ingrese 'salir' para volver al menu principal")
        opcion1 = input("Ingrese una opcion: ").strip()
        if (opcion1 == "1"):
            ReporteCancionesMasSonadas()
        elif opcion1 == "2":
            print("") #Falta Implementar
        elif opcion1 == "3":
            print("") #Falta Implementar
        elif opcion1 == "salir":
            continue;
        else:
            print("Opcion Incorrecta")


