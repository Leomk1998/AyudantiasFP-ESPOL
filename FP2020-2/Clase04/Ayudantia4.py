# Ayudantias 13/11/2020

"""
string = "Leonardo"
numeroDC = len(string)
print("len:",len(string))

def miLen(string):
    contador=0
    for carater in string:
        contador+=1
    return contador
print("Mi len:",miLen(string))
"""
"""
#Ejercicio1
#1
def saludo():
    print("Un saludo con todos")
    print("Sobretodo con usted")
    print()
saludo()
#2
def saludoConNombre(nombre):
    print("Un saludo para",nombre)
saludoConNombre("Carlos")
#3
def saludoConOSinNombre(nombre=""):
    if nombre=="":
        print("Saludo")
    else:
        print("Un saludo para",nombre)
saludoConOSinNombre("John")
"""

#Ejercicio2
"""
def volumenEsfera(radio):
    import math
    if(radio<0):
        return -1
    else:
        v = (4/3)*math.pi*(radio**3)
        return v
radio = float(input("Ingrese el radio de su esfera: "))
volumen = volumenEsfera(radio)
volumenDIV2 = volumenEsfera(radio/2)
print(volumen)
print(volumenDIV2)
"""

#Ejercicio3
"""
#[2,3,3,3,2,1,3,5,7,5]
def listaSinRepetir(listaClq):
    listaNueva = []
    for numero in listaClq:
        if(numero not in listaNueva): #[2,3,1]
            listaNueva.append(numero)
    return listaNueva
listaSinRep = listaSinRepetir([2,3,3,3,2,1,3,5,7,5])
print(listaSinRep)
"""

#Ejercicio4
#["Leonardo Mendoza","Luis Garcia", "Ethiel Cajas","Leonardo Garcia"]
"""
def buscar(arreglo, nombreABuscar=""):
    nombresEncontrdos = []
    for nombreCompleto in arreglo:
        if(nombreABuscar.lower() in nombreCompleto.lower()):
            nombresEncontrdos.append(nombreCompleto.title().replace(" ",""))
    return nombresEncontrdos
lista = buscar(["Leonardo Mendoza","Luis Garcia", "Ethiel Cajas","Leonardo Garcia"],"cajas")
print(lista)
"""
#Ejercicio5
"""
def esPalindromo(palabra):
    palabraProcesada = palabra.lower().replace(" ","")
    palabraAlReves = palabraProcesada[::-1]
    if(palabraProcesada==palabraAlReves):
        return True
    else:
        return False
palabra = "Mi casa es comoda"
print(esPalindromo(palabra))
"""
#Ejercicio6
"""
def histograma(datos):
    caracter = input("Ingrese un caracter:")
    while len(caracter)!=1:
        caracter = input("Ingrese un caracter:")
    print("Histograma:")
    for numero in datos:
        print(caracter*numero)
    return None
histograma([4,8,5,2,3,12])


def histograma1(*datos):
    caracter = input("Ingrese un caracter:")
    while len(caracter)!=1:
        caracter = input("Ingrese un caracter:")
    print("Histograma:")
    for numero in datos:
        print(caracter*numero)
    return None
histograma1(1,5,6,7,34,7,34,3)
"""
#Ejercicio 7
"""
def sumador(caracter,*numeros):
    print(caracter)
    return sum(numeros)
print(sumador("hola",10,20,30,40,2,3,1,2,3,4,5))
"""
#Ejercicio 8
"""
def maxMinProm(*numeros):
    maximo = max(numeros)
    minimo = min(numeros)
    prom = sum(numeros)/len(numeros)
    return maximo,minimo,prom
valores = maxMinProm(10,20,30,40,2,3,1,2,3,4,5)
print(valores)
"""


lista = ['Luis','Rafael','Diego','Carlos','Rodrigo','Steven','Jose','Miguel','Luka','Jorge','Mike','Ibai']
for nombre in lista:
    fin=True
    for letra in nombre:
        if(fin):
            print(letra)
        if(letra in "aeiou"):
            fin=False
print("Fin del programa")
n=0
while n!=10:
    n+=1
    print(n)
    if(n==5):
        n=10
print("Fin del programa")