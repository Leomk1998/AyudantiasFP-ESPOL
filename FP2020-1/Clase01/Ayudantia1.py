'''
#taller

# Validar una cedula
# Las condiciones son:
#1. La cédula debe contener solo números, no puede tener letras
#2. La cédula debe tener 10 dígitos exactos
#3. La cédula debe ser de Gye (09), empezar con estos dígitos
#4. Solicite la cédula y presente un mensaje personalizado.
#Ejm: La cédula 092821928a es correcta? False.
#NOTA: Para que sea True debe cumplir todas las condiciones.
#Hola
print("*******Validacion de Cedula************")
cedula=input("Ingrese su cedula: ")
val1= cedula.isdigit()
val2= len(cedula)==10
val3= cedula.startswith("09")
valGeneral = val1 and val2 and val3
print("Cedula valida?", valGeneral)

# Validar un correo ESPOL
# Las condiciones son:
#1. El correo debe terminar en espol.edu.ec
#2. El correo debe tener un @
#3. El correo debe empezar con una letra
#4. El usuario de correo no podría ser espol: espol@espol.edu.ec no sería correcto
#5. Solicite el correo y presente un mensaje personalizado.
#Ejm: El correo felipe2@fiec.espol.edu.ec pertenece a ESPOL? True.
#NOTA: Para que sea True debe cumplir todas las condiciones.

# hola@hola@espol.edu.ec

print("Validador de correos ESPOL")
correoEntrada=input("Ingrese su correo: ")
val1=correoEntrada.endswith("espol.edu.ec")
val2=correoEntrada.count("@")==1
val3=correoEntrada[0].isalpha()
val4= not (correoEntrada[0:correoEntrada.find("@")] == "espol")
valgeneral=val1 and val2 and val3 and val4
print("El correo es valido?",valgeneral)


#Ejercicio 1

#f=78
f=int(input("Ingrese la temperatura en grados Farhenheit: "))
c=(f-32)*5/9
print("%d grados Farhenheit son %d grados centigrados"%(f,c))


#Ejerciicio 2
segundosUsuario=int(input("Ingrese una cantidad de segundos: "))
horas=segundosUsuario//3600
minutos=(segundosUsuario%3600)//60
segundos=(segundosUsuario%60)

print("%d segundos son %d hora(s), %d minuto(s), %d segundo(s)"%(segundosUsuario,horas,minutos,segundos))

#Ejercicio 3

print("***********Juego de Adivinanza*************")
print("La palabra a adivinar es: 'P______r' ")
print("PISTA: se dedica profesionalmente a la enseñanza")
palabraUsuario=input("Ingrese la palabra que usted cree que es: ").title().strip()
palrabra = "Profesor"
val = palrabra.title() == palabraUsuario
print("Adivino?",val)



print("PROGRAMA PARA VER SI REPROBASTE")
par1=int(input("Ingrese su nota de primer parcial: "))
par2=int(input("Ingrese su nota de segundos parcial: "))
mej=int(input("Ingrese su nota de mejoramiento: "))
prac=int(input("Ingrese su nota practica: "))
clases=int(input("Ingrese su numero total de clases: "))
faltas=int(input("Ingrese su numero de faltas: "))
#listaTeorico=[(par1+par2)/2,(par1+mej)/2,(par2+mej)/2]
promedioTeorico=max((par1+par2)/2,(par1+mej)/2,(par2+mej)/2)
promedioGeneral=(promedioTeorico*0.8)+(prac*0.2)
porcentajeAsistencias = ((clases-faltas)/clases)*100
val = (promedioGeneral<60) or (porcentajeAsistencias<60)
print("Su promedio es {0:.1f}, su cantidad de faltas {2} y su porcentaje de asistencia {1:.1f} %".format(promedioGeneral,porcentajeAsistencias,faltas))
print("Reprobado?",val)



#Ejercicio 5

print("Este es un mensaje\n\n\tQue usa caracteres especiales\n\nEn un solo string.")


#Ejercicio 6

import random

lista=['Luis','Rafael','Diego','Carlos','Rodrigo','Steven','Jose','Miguel','Luka','Jorge','Mike','Ibai']
print("Programa de Sorteo de Electrodomesticos")
#primerGanador = random.choice(lista)
primerGanador = lista[random.randint(0,len(lista)-1)] #randint [A,B]      ranrange[A,B)
print("Primer Ganador es",primerGanador,"y se lleva una licuadora.")
#segundoGanador = random.choice(lista)
segundoGanador = lista[random.randint(0,len(lista)-1)] #randint [A,B]      ranrange[A,B)
print("Segundo Ganador es",segundoGanador,"y se lleva una freidora de aire.")
#tercerGanador = random.choice(lista)
tercerGanador = lista[random.randrange(0,len(lista))] #randint [A,B]      ranrange[A,B)
print("Tercer Ganador es",tercerGanador,"y se lleva una refrigeradora.")



#Ejercicio 7

import random
lista=["Jose",'Rafael','Diego','Carlos','Rodrigo','Steven','Jose','Miguel','Luka','Jorge','Mike','Ibai']

print("Sorteo de paracaidas")
primerGanador=lista.pop(random.randint(0,len(lista)-1)) #lista.pop(i) pop elimina el elemento del indice i de a lista, y de devuelve
print(primerGanador,"ha saltado en paracaidas.")
segundoGanador=lista.pop(random.randrange(0,len(lista)))
print(segundoGanador,"ha saltado en paracaidas.")
tercerGanador=lista.pop(random.randrange(0,len(lista)))
print(tercerGanador,"ha saltado en paracaidas.")
print("Lista de los que saltaron en el avion: ")
print(lista)


listaEstudiante=["Jose",'Rafael','Diego','Carlos','Rodrigo']
listaNuevosEstudiantes=['Steven','Jose','Miguel','Luka','Jorge','Mike','Ibai']
listaEstudiante.extend(listaNuevosEstudiantes)
print(listaEstudiante)

num = "63.3333333333333"
# num1 = num[0:2] #si conoces la cantidad de digitos del numero
num1 = float(num[0:num.find(".")+3])
lista= []
lista.append(float(num1))
print(lista)


#Ejercicio 6

import random

lista=['Luis','Rafael','Diego','Carlos','Rodrigo','Steven','Jose','Miguel','Luka','Jorge','Mike','Ibai']
print("Programa de Sorteo de Electrodomesticos")
#primerGanador = random.choice(lista)
primerGanador = lista[random.randint(0,len(lista)-1)] #randint [A,B]      ranrange[A,B)
print("Primer Ganador es",primerGanador,"y se lleva una licuadora.")
#segundoGanador = random.choice(lista)
segundoGanador = lista[random.randint(0,len(lista)-1)] #randint [A,B]      ranrange[A,B)
print("Segundo Ganador es",segundoGanador,"y se lleva una freidora de aire.")
#tercerGanador = random.choice(lista)
tercerGanador = lista[random.randrange(0,len(lista))] #randint [A,B]      ranrange[A,B)
print("Tercer Ganador es",tercerGanador,"y se lleva una refrigeradora.")


listaEstudiante=["Jose",'Rafael','Diego','Carlos','Rodrigo']
listaEstudiante[0]="Pepe"
print(listaEstudiante)

'''