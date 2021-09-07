# Ayudantia 18/06/2021
"""
# #Funcionesprint(len("Leonardo"))
def lenHechoPorMi(Iterable):
    tamano = 0    for elemento in Iterable:
        tamano += 1    return tamanoprint(lenHechoPorMi("Leonardo"))
#Ejercicio 1:#1def saludo():
    print("Muy buenos días. Ante todo, un cordial saludo a todas y todos ustedes y en forma muy especial a los Ministros")
    return#print(type(saludo()))#2nombre = "Leonardo"def saludo(nombre):
    print("Muy buenos días. Ante todo, un cordial saludo a todas y todos ustedes y en forma muy especial a %s"%(nombre))
    returnsaludo("Selena")
saludo("Kevin")
#3def saludo(nombre=""):
    if nombre != "":
        saludo = "Muy buenos días. Ante todo, un cordial saludo a todas y todos ustedes y en forma muy especial a %s" % (nombre)
    else:
        saludo = "Saludos"    return saludoprint(saludo())
s = saludo("Leonardo")
print(s)
print(s*3)
#Ejercicio 2import mathprint(math.pi)
def volumenEsfera(radio):
    if radio > 0:
        volumen = (4/3)*math.pi*(radio**3)
    else:
        volumen = -1    return volumenprint(volumenEsfera(5))
print(volumenEsfera(1))
print(volumenEsfera(2))
#Ejercicio 3# [1,2,3,4,5,1,3,5]# [1,2,3,4,5]def listaSinRepetidos(lista):
    listaNueva = []
    for elemento in lista:
        if(elemento not in listaNueva):
            listaNueva.append(elemento)
    return listaNuevaprint(listaSinRepetidos([5,19,23,53,2,5,4,2,3,9,8]))
print(listaSinRepetidos([5,1,2,5,2,5,4,2,3,9,8]))
#Ejercicio 4# ["LeoNardo MendOza","Antonio ValEncia   ","   Leonardo Di Caprio   ","Enner Valencia   ", "Leonel Messi    "]# "Valencia"def buscar(lista, nombreABuscar):
    nombresCo = []
    for nombresCompletos in lista:
        nombresCompletoCorregido = nombresCompletos.title().strip() #Antionio, Leonardo         nombreABuscarCorregido = nombreABuscar.title().strip() # A        if(nombreABuscarCorregido.lower() in nombresCompletoCorregido.lower()):
            nombresCo.append(nombresCompletoCorregido)
    return nombresConombres = ["LeoNardo MendOza","Antonio ValEncia   ","   Leonardo Di Caprio   ","Enner Valencia   ", "Leonel Messi    "]
nombre = "ValeNcIa"print(buscar(nombres,"l"))
# Ejercicio 5def esPalindromo(frase):
    #lista = frase.split(" ")    #print(lista)    #frase = "".join(lista)    #print(frase)    frase = frase.replace(" ","")
    #print(frase)    fraseAlReves = frase[::-1]
    if(frase.lower() == fraseAlReves.lower()):
        return True    else:
        return Falseprint(esPalindromo("Amor a Roma"))
print(esPalindromo("Oso"))
print(esPalindromo("Se van sus naves"))
print(esPalindromo("Osos"))
# Ejercicio 6def histograma(datos):
    entrada = ""    while len(entrada)!=1:
        entrada = input("Ingrese un carácter: ")
    for numero in datos:
        print(entrada*numero)
histograma([10,11,14,3,1,8,5,2,3,12])
#Solucion Carlosdef sumador():
    numero = ""    suma = []
    while numero != 0:
        numero = int(input("ingrese un número: "))
        suma.append(numero)
    return sum(suma)
resultado = sumador()
print("la suma de todos los numeros ingresado es:", resultado)
# sumador(2,4,5,6,7,34,5345,34,53,45,34,5,345,34,53,45,34,5,345,34,53,45,34,5)def sumador(Clave,*numeros):
    print(Clave)
    return sum(numeros)
print(sumador("Clave1",1,2,3))
print(sumador("Clave2",2,4,5,6,7,34,5345,34,53,45,34,5,345,34,53,45,34,5,345,34,53,45,34,5))
print(sumador("Clave3"))
def programa():
    numero = ""    suma = []
    while numero != 0:
        suma.append(numero)
    for i in range(10):
        sumador("Clave",suma)
def juegoPPT():
    #codigo    op1 = sacarOpcion(Jugador1)
    op2 = sacarOpcion(Jugador2)
    ganador = Comparar(op1,op2)
    return ganadorjuegoPPT()
sacarOpcion(Jugador1)
sacarOpcion(Jugador2)
# Ejercicio 8def maxMinProm(*numeros):
    maximo = max(numeros)
    minimo = min(numeros)
    promedio = sum(numeros)/len(numeros)
    return maximo,minimo,promediomaximo,minimo,promedio = maxMinProm(4545,4545,44864,854547)
print("Max:",maximo)
print("Min:",minimo)
print("Prom:",promedio)
print(maxMinProm(4545,4545,44864,854547))

import random
def juegoPPT():
    jugador1 = random.randint(1,3)
    jugador2 = random.randint(1,3)
    opciones = ["piedra","papel","tijera"]
    print("Jugador1:",jugador1)
    print("Jugador2:", jugador2)
    if(jugador1==jugador2):
        print("Empate")
    elif(jugador1==1):
        if (jugador2==2):
            print("Papel le gana a piedra")
            print("Jugador 2 gana")
        elif (jugador2 == 3):
            print("Piedra le gana a tijera")
            print("Jugador 1 gana")
    elif (jugador1 == 2):
        if (jugador2 == 1):
            print("Papel le gana a piedra")
            print("Jugador 1 gana")
        elif (jugador2 == 3):
            print("Tijera le gana a papel")
            print("Jugador 2 gana")
    elif (jugador1 == 3):
        if (jugador2 == 1):
            print("Piedra le gana a tijera")
            print("Jugador 2 gana")
        elif (jugador2 == 2):
            print("Tijera le gana a papel")
            print("Jugador 1 gana")
juegoPPT()


def juegoPPTmin():
    jugador1 = random.randint(1, 3)
    jugador2 = random.randint(1, 3)
    if (jugador1 == 1 and jugador2==2) or (jugador1 == 2 and jugador2==1):
        print("Papel le gana piedra")
    elif (jugador1 == 1 and jugador2==3) or (jugador1 == 3 and jugador2==1):
        print("Papel le gana piedra")
    elif (jugador1 == 3 and jugador2==2) or (jugador1 == 2 and jugador2==3):
        print("Papel le gana piedra")
    else:
        print("Empate")
"""