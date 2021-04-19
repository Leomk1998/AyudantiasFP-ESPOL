# 06/11/2020
# Ayudante: Leonardo Mendoza

#Ejercicio 1

#range() [0,1,2...n-1]
"""
for i in range(101):
    print(i)
"""

#Ejercicio 2

"""
for i in range(1,101):
    print(i)
"""

#Ejercicio 3
"""
for i in range(0,101,2):
    print(i)
"""
"""
for i in list(range(0,101))[::-1]:
    print(i)
"""

#Ejercicio 4

"""
numeros = []
entrada = int(input("Ingrese un numero al sumador o 0 para salir: "))
while not entrada == 0:
    numeros.append(entrada)
    entrada = int(input("Ingrese un numero al sumador o 0 para salir: "))
print(numeros)
print("La suma de esos numeros es",sum(numeros))
"""

#Ejercicio 5

"""
print("Politechicos: ")
print("Perdí un iPhone en biblioteca. \nTengo video de la cámara de seguridad,por favor devuelve lo que te llevaste")
comentario = input("Ingrese su comentario: ")
repeticiones = int(input("Cuántas personas han comentado: "))
for i in range(1,repeticiones+1):
    print(comentario,end=" ")
    if i!=1:
        print("x%d"%i)
    else:
        print()
print("Fin.")
"""

#Ejercicio 6

"""
listaNotas = []
numerosTalleres = input("¿Cuantos talleres ha dado? ")
while not numerosTalleres.isdigit():
    print("No ingreso un numero, intente otra vez")
    numerosTalleres = input("¿Cuantos talleres ha dado? ")
numerosTalleres = int(numerosTalleres)
for i in range(1,numerosTalleres+1):
    notaTaller = input("Ingrese la nota del taller %d:"%i)
    while not(int(notaTaller)>=0 and int(notaTaller)<=100):
        print("No ingreso un numero correcto, intente otra vez")
        notaTaller = input("Ingrese la nota del taller %d:" % i)
    notaTaller = int(notaTaller)
    listaNotas.append(notaTaller)
# [100,10,100,20,90]
tallerMasBajo = min(listaNotas)
#listaNotas.pop(listaNotas.index(tallerMasBajo))
listaNotas.remove(tallerMasBajo)
print("Taller mas bajo: ",tallerMasBajo)
print("Nota de los talleres: ",listaNotas)
print("Promedio: ",sum(listaNotas)/len(listaNotas))
"""

#Ejercicio 7

"""
username = input("Ingrese su nombre de usuario de instagram: ")
for carater in username:
    print("El caracter {}".format(carater),end=" ")
    if carater.isdigit():
        print("es un numero")
    elif carater.upper() in "AEIOU":
        print("es una vocal")
    elif carater in "_-. ":
        print("es un signo")
    else:
        print("es una consonante")
print("Fin del programa.")
"""


#Ejercicio 8

"""
print("***Validador de correos espol***")
valtotal = False
while not valtotal:
    correo = input("Ingrese su correo espol: ")
    val1 = correo.endswith("espol.edu.ec")
    val2 = correo.count("@") == 1
    val3 = correo[0].isalpha()
    val4 = correo[0:correo.find("@")]!="espol"
    valtotal = val1 and val2 and val3 and val4
print("Correo valido")
"""

#Ejercicio 9

#Imprimir instrucciones
opcion = 0
while opcion!=5:
    print("********Menu de operaciones*****-***")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplica")
    print("4. Division")
    print("5. salir")
    opcion = int(input("Ingrese una opcion del menu: "))
    if opcion==1:
        num1=int(input("Ingrese un numero:"))
        num2 = int(input("Ingrese otro numero:"))
        print("La suma es ", num1+num2)
    elif opcion==2:
        print("restando")
    elif opcion==3:
        print("multiplicando")
    elif opcion==4:
        print("div")
    elif opcion==5:
        print("Saliendo del programa")
    else:
        print("opcion incorrecta")
print("Fin del programa")
print()