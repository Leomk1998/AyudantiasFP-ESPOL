# Ayudantia: 20/11/2020

#Ejercicio1
"""
def totalpalabras(mensaje):
    mensaje = mensaje.replace(","," ").replace("."," ")
    listaPalabras = mensaje.split(" ")
    numeroPalabras = len(listaPalabras)
    return numeroPalabras
m = "Hola como estas,yo estoy muy bien"
print(totalpalabras(m))
"""
#Ejercicio2
"""
def traductor_esp_qui(palabra, modo):
    quichua = ['man', 'wasi', 'pak', 'kuska', 'pash', 'iyayku', 'mañay', 'mamallakta', 'kutipak']
    espanol = ['al', 'casa', 'del', 'lugar', 'y', 'tecnología', 'servicio', 'país', 'traductor']
    if(modo==1):
        if palabra.lower() in quichua:
            traduccion = espanol[quichua.index(palabra)]
            return traduccion
        else:
            print("no se encuentra la palabra")
            return "error"
    elif(modo==2):
        if palabra.lower() in espanol:
            traduccion = quichua[espanol.index(palabra)]
            return traduccion
        else:
            print("no se encuentra la palabra")
            return "error"
    else:
        print("Modo no valido")
        return "error"
print(traductor_esp_qui("ciudad",2))
"""
#Ejercicio3
"""
from random import * #choice() randint() etc.
#import random # random.choice random.randint
def bautizarRobots(tam):
    letras = 'abcdefghijklmnñopqrstuvwxyz'
    numeros = '1234567890'
    nombre = ""
    for i in range(tam):
        if(i%2==0):
            nombre+= choice(letras).upper()
        else:
            nombre+= choice(numeros)
    return nombre
print(bautizarRobots(9))
"""
#Ejercicio4
"""
#[Leonardo,Jared,Carlos,Luis, Gabriel] entrada
#[[Leonardo, Jared],[Jared, Carlos],[Carlos, Leonardo]] salida
import random
def amigoSecreto(listaAmigos):
    listaRetorno = []
    copiaLista = listaAmigos.copy()
    primerAS = copiaLista.pop(random.randint(0,len(copiaLista)-1))
    primero = True
    asActual = ""
    while len(copiaLista) !=0 :
        AS = copiaLista.pop(random.randint(0,len(copiaLista)-1))
        if(primero):
            listaRetorno.append([primerAS,AS])
            primero = False
        else:
            listaRetorno.append([asActual,AS])
        asActual = AS
    listaRetorno.append([asActual,primerAS])
    return listaRetorno
listaAmigos = ['Luis','Rafael','Diego','Carlos','Rodrigo','Steven','Jose','Miguel','Luka','Jorge','Mike','Ibai']
print(amigoSecreto(listaAmigos))
"""
#Ejercicio5

def imprimirMenu():
    print("""Menú para saber cuanto vas a gastar en el supermercado antes de ir a la caja:
1. Agregar producto.
2. Imprimir detalle.
3. Salir.""")
"""
def agregarProducto(ListaNombre,ListaCantidad,ListaPrecios,ListaIVA):
    ListaNombre.append(input("Ingrese el nombre del producto: "))
    ListaCantidad.append(int(input("Ingrese la cantidad: ")))
    ListaPrecios.append(float(input("Ingrese el precio unitario: ")))
    iva = input("Ingrese si su producto paga iva (si/no): ").lower().strip()
    if(iva=="si"):
        ListaIVA.append(True)
    else:
        ListaIVA.append(False)
def subTotal(ListaNombre,ListaCantidad,ListaPrecios,ListaIVA):
    subTotalConIVA=0
    subTotalSinIVA=0
    for i in range(len(ListaNombre)):
        if ListaIVA[i]:
            subTotalConIVA += ListaPrecios[i]*ListaCantidad[i]
        else:
            subTotalSinIVA += ListaPrecios[i]*ListaCantidad[i]
    return subTotalSinIVA,subTotalConIVA

def imprimirDetalle(ListaNombre,ListaCantidad,ListaPrecios,ListaIVA):
    print()
    print("%-15s %-15s %-15s"%("Cantidad","Item","Precio"))
    for i in range(len(ListaNombre)):
        if(ListaIVA[i]):
            print("%-15d %-15s %-15.2f"%(ListaCantidad[i],ListaNombre[i],ListaCantidad[i]*ListaPrecios[i]))
        else:
            print("%-15d %-15s %-15.2f %s"%(ListaCantidad[i],ListaNombre[i],ListaCantidad[i]*ListaPrecios[i],"NO IVA"))
    subTotalSinIva,subTotalConIva = subTotal(ListaNombre,ListaCantidad,ListaPrecios,ListaIVA)
    print("\t %-30s     %.2f"%("SUBTOTAL(SIN IVA)",subTotalSinIva))
    print("\t %-30s     %.2f" % ("SUBTOTAL(CON IVA)", subTotalConIva))
    print("\t %-30s     %.2f" % ("IVA A PAGAR", subTotalConIva*0.12))
    print("\t %-30s     %.2f" % ("TOTAL A PAGAR", subTotalSinIva+(subTotalConIva*1.12)))
    print()

opcion=4
listaNombres = []
listaCantidades = []
listaPrecios = []
listaIVA = []
while opcion!=3:
    imprimirMenu()
    opcion = int(input("Ingrese una opcion: "))
    if(opcion==1):
        agregarProducto(listaNombres,listaCantidades,listaPrecios,listaIVA)
    elif(opcion==2):
        imprimirDetalle(listaNombres, listaCantidades, listaPrecios, listaIVA)
    elif(opcion==3):
        print("Fin del programa")
    else:
        print("Opcion incorrecta.")
"""
import random
def numeroAlAzar():
    numeroInterno = random.randint(0,10)
    n = 5
    return numeroInterno,n

def sumarNumeros(n1,n2):
    return n1+n2

numeroExterno,n = numeroAlAzar()
print(numeroExterno)
print(sumarNumeros(numeroExterno,numeroExterno))
print(n)