#Ayudantia 2

#Revision literal 10 ejercicio anterior

cantantes = ["Dua Lipa","Bruno Mars","Ariana Grande","Luis Fonsi","The Weekend","Bad Bunny", "Tones and I"]
genero = ["f","m","f","m","m","m","f"]
discos = [3,8,5,14,5,4,1]
instagram = [46.9, 22.3, 50, 15.6, 20.1, 28, 10.5] #millones

#10. Ejemplo mejorado del primer literal
print("\n10. Agregar nuevos cantantes")  # dar enter

cont = input("¿Cuántos desea agregar? ")
while not cont.isdigit():
    cont = input("¿Cuántos desea agregar? ")
cont = int(cont)

for i in range(cont):
    cantante = ""
    while cantante in cantantes or cantante=="":
        cantante = input("Ingrese un cantante: ")
    if cantante not in cantantes:
        cantantes.append(cantante)
        genero.append(input("Ingrese su genero f/m: ").lower())
        discos.append(int(input("Ingrese nro discos: ")))
        instagram.append(float(input("Ingrese seguidores: ")))
input("Se agregaron {} nuevos cantantes: {}".format(cont, cantantes[-cont:]))
print("Lista actual",cantantes)


#Ejercicio 1
horaUsuario = input("Ingresa la hora (HH:MM): ")
while not (len(horaUsuario)==5 and horaUsuario.count(":")==1): #not (a and b) = (not b or not a)
    print("Formaro Incorrecto")
    horaUsuario = input("Ingresa la hora (HH:MM): ")
hora = horaUsuario.partition(":")[0]
inthora = int(hora)
if(inthora<12):
    print("ES A.M.")
elif(inthora<24):
    print("ES P.M")
else:
    print("Hora invalida")


#Ejercicio 2
import random
print("JUEGO DEL PENALTI")
tiroUsuario = input("Escoja su zona de lanzamiento [1,6]: ")
while not tiroUsuario.isdigit():
    print("Error, no ingreso un numero.")
    tiroUsuario = input("Escoja su zona de lanzamiento [1,6]: ")

numerotiro=int(tiroUsuario)
while not (numerotiro>=1 and numerotiro<=6):
    print("Error: Numero fuera del rango")
    tiroUsuario = int(input("Escoja su zona de lanzamiento [1,6]: "))
    numerotiro = int(tiroUsuario)
portero = random.randint(1,6)
print("EL PORTERO SE LANZO A",portero)
if(portero == numerotiro):
    print("NO ES GOL")
else:
    print("ES GOL")
    if (numerotiro in [3,4]):
        print("Por izquierda")
    elif (numerotiro in [2,5]):
        print("Por centro")
    elif (numerotiro in [1,6]):
        print("Por derecha")


#ejercico 3

print("SUPERMERCADO: DESCUENTO")
producto= "Galletas Oreo en Tubo"
print("Producto:",producto)
precio= 0.9
print("Si compra mas de tres docenas tiene %15 de descuento")
print("Caso contrario tiene 10% de descuento")
numeroCliente=input("Ingrese la cantidad que quiere comprar: ")
while not (numeroCliente.isdigit()):
    print("No ingreso un numero, error")
    numeroCliente = input("Ingrese la cantidad que quiere comprar: ")
numCliente = int(numeroCliente)
if(numCliente < 36):
    descuento = 0.10
    descuentoTotal = (descuento*precio)*numCliente
    total = (numCliente*precio) - (descuentoTotal)
    print("Descuento: {0:.2f}".format(descuentoTotal))
    print("Total:",total)
else:
    descuento = 0.15
    descuentoTotal = (descuento * precio) * numCliente
    total = (numCliente * precio) - (descuentoTotal)
    print("Descuento: {0:.2f}".format(descuentoTotal))
    print("Total:", total)
    obsequios = (numCliente//12)
    print("Obsequio {0} productos".format(obsequios))


#Ejercicio 4

#range(m,n) = [m,...,n-1]
for numero in range(1,101): #range(101) = [0,1,2,4,...,10]  #range(n) = [0,1,2,4,...,n-1]
    print(numero)

for numero in range(0,102,2): #range(m,n,s) = [m, m+s , ... m+s<n]
    print(numero)

#Ejercicio 6

for numero in range(1,100,2): #range(m,n,s) = [m, m+s , ... m+s<n]
    print(numero)

for numero in range(1,100):
    if(numero%2==1):
        print(numero)


#Ejercicio 7

print("SUMADOR DE NUMEROS")
numeros=[]
entrada = int(input("Ingrese un numero (0 para salir): "))
while not entrada ==0:
    numeros.append(entrada)
    entrada = int(input("Ingrese un numero (0 para salir): "))
print("La sumatoria es",sum(numeros))


#Ejercicio 8

numero = input("Ingrese un numero de cifras impares: ")
while not (numero.isdigit()):
    print("No es un numero")
    numero = input("Ingrese un numero de cifras impares: ")
num = int(numero)
while num%2==0:
    print("No es un numero impar")
    num = input("Ingrese un numero de cifras impares: ")
val=True
for i in range(len(str(numero))-1):
    if not(numero[i]==numero[len(numero)-1-i]):
        val=False
print("El numero es igual al reves y al derecho?",val)


#Ejercicio 9

lista=[]
numeroTalleres = input("Cuantos talleres tiene?")
while not numeroTalleres.isdigit():
    numeroTalleres = input("Cuantos talleres tiene?")
numeroTalleres = int(numeroTalleres)
for i in range(1,numeroTalleres+1):
    notataller=input("Ingrese la nota del taller{0}: ".format(i))
    while not (notataller.isdigit()):
        notataller = input("Ingrese la nota del taller{0}: ".format(i))
    notataller = int(notataller)
    lista.append(notataller)
tallermasbajo=min(lista)
lista.remove(tallermasbajo)
promedio = sum(lista)/len(lista)
print("Promedio:",promedio)
print("Notas de Talleres:",lista)




