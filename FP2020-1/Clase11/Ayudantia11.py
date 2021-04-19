# Leonardo Mendoza
# Ayudantia: 29-Ago-2020

# Ejercicio 1
# Cargar el archivo "day_wise_ecuador.txt" en un diccionario con el siguiente formato:
# {"2020-01-22": {"total":{"Confirmed":0,"Deaths":0,...},"diario":{{"new cases":0,"new deaths":0,...}}


archivoEcuador = open("day_wise_ecuador.txt","r")
cabecera = archivoEcuador.readline()
leido = archivoEcuador.readlines()
dicc = {}
for linea in leido:
    linea = linea.replace("\n","")
    listaLinea = linea.split(",")
    dicc[listaLinea[0]]={"total":{"contagiados":listaLinea[1],"muertes":listaLinea[2],
                         "recuperados":listaLinea[3]},"diario":{"contagiados":listaLinea[4],
                        "muertes":listaLinea[5]}}
print(dicc)


# Ejercicio 2
# Escribir una funcion que retorne la cantidad de fechas que hay cargadas
# en un diccionario


def numeroDeFechas(diccionario):
    #print(diccionario.keys())
    listaClaves = list(diccionario.keys())
    sizeClaves = len(listaClaves)
    return sizeClaves

print(numeroDeFechas(dicc))

# Ejercicio 3
# Consullte los datos de contagiados y muertos de la ultima fecha cargada en el diccionario

listaClaves = list(dicc.keys())
print("Contagiados:",dicc[listaClaves[-1]]["total"]["contagiados"])
print("Muertos:",dicc[listaClaves[-1]]["total"]["muertes"])

#print(max(dicc))
claveMaxima = max(dicc)
print("Contagiados:",dicc[claveMaxima]["total"]["contagiados"])
print("Muertos:",dicc[claveMaxima]["total"]["muertes"])


# Ejercicio 4
# Escribir una funcion que reciba un diccionario day_wise y string de fecha
# e imprima los datos de esa fecha


def consultarPorFecha(diccionario,fecha):
    print("***Consulta de Datos****")
    datos = diccionario[fecha]
    print("Contagios Totales: ",datos["total"]["contagiados"])
    print("Muertes Totales: ", datos["total"]["muertes"])
    print("Total de recuperados: ",datos["total"]["recuperados"])
    print("Contagios de hoy: ", datos["diario"]["contagiados"])
    print("Muertes de hoy: ", datos["diario"]["muertes"])
fechaUsuario=input("Ingrese una fecha(aaaa-mm-dd): ")
consultarPorFecha(dicc,fechaUsuario)


# Ejercicio 5
# Escribir una funcion que reciba un diccionario day_wise e imprima los datos de una
# fecha aleatoria


import random
listaClaves = list(dicc.keys())
claveAleatoria = listaClaves[random.randint(0,len(listaClaves)-1)]
print(claveAleatoria)
print(dicc[claveAleatoria])


# Ejercicio 6
# Consulte en el diccionario la fecha con el mayor numero de nuevos contagios en Ecuador.


claveMaxima=""
valorMaximo=0
for fecha in dicc:
    if int(dicc[fecha]["diario"]["contagiados"])>int(valorMaximo):
        claveMaxima=fecha
        valorMaximo=dicc[fecha]["diario"]["contagiados"]
print("El dia que hubo mas contagios fue",claveMaxima,"con",valorMaximo)



# Examen 20171 mejoramiento


import numpy as np

M = np.array([[7,7,19,15,17,13,13],[53,195,120,150,123,60,75],[53,195,120,150,123,60,75],[53,195,120,150,123,60,75],[0.5,1.2,1.8,1.2,2,1,1]],float)
print(M)
huracanes = { 2015: ('Ana','Kate'),2017: ('Arlene','Harvey','Irma'),2016: ('Alex','Otto')}
'''
1. VV < 100 kph
2. VV de 100 a 150 kph
3. VV de 150 a 200 kph
4. VV de 200 a 250 kph
5. VV > 250 kph
3[2]
'''

#Literal 1

def total_marejada(M, cat):
    total = 0
    vv = M[2]
    if(cat==1):
        for i in range(len(vv)):
            if(vv[i]<100):
                total+=M[4][i]
    elif (cat == 2):
        for i in range(len(vv)):
            if (vv[i]>=100 and vv[i]<150):
                total += M[4][i]
    elif (cat == 3):
        for i in range(len(vv)):
            if (vv[i] >= 150 and vv[i] < 200):
                total += M[4][i]
    elif (cat == 4):
        for i in range(len(vv)):
            if (vv[i] >= 200 and vv[i] <= 250):
                total += M[4][i]
    elif (cat == 5):
        for i in range(len(vv)):
            if (vv[i] > 250):
                total += M[4][i]
    return total
print(total_marejada(M,1))

def indices_año(huracanes, año):
    inicio = min(huracanes)
    fin = max(huracanes)
    lista = []
    indice=0
    while(inicio<fin+1):
        if(inicio==año):
            lista.append(indice)
            indice+=len(huracanes[inicio])
            lista.append(indice)
        else:
            indice += len(huracanes[inicio])
        inicio+=1
    return tuple(lista)
print(indices_año(huracanes,2017))

def velocidad_superior(M, huracanes, año):
    indices = indices_año(huracanes,año)
    velocidadd = M[0,indices[0]:indices[1]]
    promedio = np.mean(velocidadd)
    contador=0
    for elem in velocidadd:
        if(elem>promedio):
            contador+=1
    return contador
print(velocidad_superior(M,huracanes,2016))

#cantidad_energia = 10^-4 * (VV1^2 + VV2^2 + … + VVn^2)
def ACE(M, huracanes, año):
    indices = indices_año(huracanes,año)
    vv = M[2,indices[0]:indices[1]]
    cantidadEnergia = (10**-4)
    suma = 0
    for valor in vv:
        suma += valor**2
    cantidadEnergia *= suma
    return cantidadEnergia
print(ACE(M,huracanes,2017))
