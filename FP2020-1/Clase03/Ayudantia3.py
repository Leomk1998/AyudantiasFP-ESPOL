#Ayudantia 27-jun-2020

#Ejercicio 1

#1
def saludo1():
    print("Saludos")
    return None
dato=saludo1()
print(dato)

n=1
while(n<100):
    n+=1
    print(n)
    if(n==10): #error
        break


#2
def saludo2(nombre):
    print("Hola",nombre)

saludo2("Leonardo")


#3
def saludo3(nombre=""):
    saludo="Hola "+nombre
    return saludo
print(saludo3("Pedro"))


#Ejercicio 2
import math
def volumenEsfera(radio):
    if(radio<=0):
        return -1
    volumen = (4/3)*math.pi*(radio**3)
    return volumen
print(volumenEsfera(10))

#Ejercicio 3

#[4,3,23,23,4,5,7]  #[4,3,23,5,7]
def enterosSinRepetir(listaEntero):
    listaRetorno=[]
    for numero in listaEntero:
        if(numero not in listaRetorno):
            listaRetorno.append(numero)
    return listaRetorno
print(enterosSinRepetir([4,3,23,23,4,5,7]))

#Ejercicio 4

#"[Leonardo Mendoza, Leonardo Ramos, Luis Garcia]"
def buscar(arreglo, nombreABuscar):
    nombresEncontrado = []
    for nombreCompleto in arreglo:
        if(nombreABuscar.lower() in nombreCompleto.lower()):
            nombresEncontrado.append(nombreCompleto.title().replace(" ",""))
    return nombresEncontrado
lista = buscar(["leonardo mENDoza", "Leonardo Ramos", "LuIs garcia"], "l")
print(lista)


#Ejercicio 5

def esPalindromo(frase):
    fraseSinEspacios= frase.replace(" ","").lower()
    retorno = True
    for i in range(len(fraseSinEspacios)):
        if(not fraseSinEspacios[i]==fraseSinEspacios[len(fraseSinEspacios)-1-i]):
            retorno=False
    return retorno
dato= esPalindromo("Amor a Roma")
print(dato)

def esPalindromo1(frase):
    fraseSinEspacios= frase.replace(" ","").lower()
    textoinv="".join(reversed(fraseSinEspacios)) #casa      reversed() = ["a","s","a","c"]  "".join()=  asac
    if(fraseSinEspacios==textoinv):
        return True
    else:
        return False
dato1= esPalindromo1("Mi casa es comoda")
print(dato1)

#[::-1] solucion alternativa


#Ejercicio 6

def histograma(listaDeNumero):
    caracter = input("Ingrese un caracter: ")
    while(not len(caracter)==1):
        caracter = input("Ingrese un caracter: ")
    print("Histograma:")
    for numero in listaDeNumero:
        print(caracter*numero)
    return None

histograma([10,12,10,8,6,4,2,0])

#Ejercicio 7

def sumador(string,*sumandos):
    suma=0
    for sumando in sumandos:
        suma+=sumando
    print(string)
    return suma
print(sumador("Hola estoy sumando"))


#Ejercicio 8

def Max_Min_Mean(*numeros):
    minimo = min(numeros)
    maximo = max(numeros)
    promedio = sum(numeros)/len(numeros)

    return maximo,minimo,promedio

max1,min1,mean1 = Max_Min_Mean(12,34,100,1,143)
print("Maximo: ",max1)
print("Minimo: ",min1)
print("Promedio: ",mean1)



#Ejercicio 9         10!=10*9*8*7*6...*1        10!=  10*9!

def factorial(numero):
    resultado=1
    for i in range(1,numero+1):
        resultado*=i
    return resultado

print(factorial(5))

def factorial1(numero): #recursividad
    if(numero==1):
        return 1
    elif(numero>1):
        return factorial(numero-1)*numero
    else:
        return None
print(factorial1(5))



#preguntas
def calcularRaiz(numero):
    return numero**0.5

def comprobarSiLaRaizDelNumeroEsMayor10(listaNumeros):
    for numero in listaNumeros:
        if(calcularRaiz(numero)>10):
            print("La raiz de",numero,"es Mayor a 10")
        else:
            print("La raiz de", numero,"no es Mayor a 10")

comprobarSiLaRaizDelNumeroEsMayor10([10,100,144])




