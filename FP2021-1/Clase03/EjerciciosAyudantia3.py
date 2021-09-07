# Ayudante: Leonardo Mendoza    11/06/2021

# Ejercicio 1

numero = 0
while numero<=100:
    print(numero)
    numero += 1 #numero = numero+1

for i in range(101): # range(n) : [0,1,...,n-1]
    print(i)

# Ejercicio 2

numero = 2
while numero<=100:
    print(numero)
    numero += 2 #numero = numero+1

# Ejercicio 3

for i in range(1,101,2): # range(valorinicial(0),valorfinal,saltos(=1)) : [0,1,...,n-1]
    print(i)

# Ejercicio 4

lista = []
numero = -1
while numero!=0:
    numero = float(input("Ingrese un numero: "))
    lista.append(numero)
print(sum(lista))

# Ejercicio 5

print("Perdí un iPhone en biblioteca. \nTengo video de la cámara de seguridad, por favor devuelve lo que te llevaste")
comentario = input("Ingrese el comentario: ")
numero = int(input("Ingrese el numero de repeticiones: "))
for i in range(numero):
    print(comentario,"x%d"%(i+1))

# Ejercicio 6

numeroDeTalleres = int(input("Ingrese cuántos talleres ha dado: "))
listaNotas = []
for i in range(numeroDeTalleres):
    nota = float(input("Ingrese la nota del taller %d: "%(i+1)))
    listaNotas.append(nota)
notaMasBaja = min(listaNotas)
numeroTaller = listaNotas.index(notaMasBaja) +1
listaNotas.remove(notaMasBaja)
print("La nota mas baja fue la del taller %d con %.2f fue elimanada"%(numeroTaller,notaMasBaja))
suma = 0
for nota in listaNotas:
    suma += nota
promedio = suma/len(listaNotas)
print("Las notas de sus talleres es",listaNotas,"y su promedio es",promedio)

# Ejercicio 7

nombreUsuario = input("Ingrese su nombre de usuario: ")
valido = True
for caracter in nombreUsuario:
    if caracter in "aeiouAEIOU":
        print(caracter,"es una vocal.")
    elif caracter.isalpha():
        print(caracter,"es una consonante.")
    elif caracter.isdigit():
        print(caracter,"es un numero.")
    elif caracter in "-_.":
        print(caracter,"es un simbolo.")
    else:
        print(caracter,"no es valido.")
        valido = False
print("Es un nombre valido?",valido)

# Ejercicio 8

val = False
while val!=True:
    correo = input("Ingrese un correo ESPOL: ")
    val1 = correo.endswith("espol.edu.ec")
    val2 = correo.count("@")==1
    val3 = correo[0].isalpha()
    val4 = correo.split("@")[0] != "espol"
    #val4 = correo[:correo.index("@")] != "espol"
    #print(val4)
    val = val1 and val2 and val3 and val4
    if (val == False):
        print("Correo no valido")

# Ejercicio 9
#Imprimir instrucciones

opcion = 0
while opcion!=5:
    print("********Menu de operaciones********")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplica")
    print("4. Division")
    print("5. salir")
    opcion = int(input("Ingrese una opcion del menu: "))
    if opcion==1:
        lista = []
        numero = -1
        while numero != 0:
            numero = float(input("Ingrese un numero: "))
            lista.append(numero)
        print(sum(lista))
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


# Solucion Taller1 e1

nombreCompleto = input("Nombre Completo:")
fechaNacimiento = input("FechaNacimiento (dd-mm-aaaa):")
nmatricula = input("Numero matricula:")
correo = input("Ingrese su email:")
materias = []
notas = []
for i in range(3):
    materias.append(input("Ingrese la materia %d:"%(i+1)))
    notas.append(float(input("Ingrese la nota nota de la materia %d:" % (i + 1))))
print("REPORTE DEL ESTUDIANTE:")
listaNombre = nombreCompleto.split(" ")
usuario = correo.split("@")[0]
listaNombre.append(usuario)
print("Nombres y usuario:",listaNombre)
mes = int(fechaNacimiento.split("-")[1])
year = int(fechaNacimiento.split("-")[2])
if(mes > 6):
    edad = 2021-year-1
else:
    edad = 2021-year
print("Edad:",edad,"años")
print("Año de ingreso:",nmatricula[0:4])
suma = 0
for nota in notas:
    suma += nota
promedio = suma/len(notas)
if(promedio>=60):
    estado = "Aprobado"
else:
    estado = "Reprobado"
print("Promedio: %.1f"%promedio)
print("Estado:",estado)

# Solucion Taller1 e2
# posible solucion 1
numero = int(input("Ingrese un numero: "))
for i in range(1,13):
    print(i,"x",numero,"=",numero*i)
# posible solucion 2
numero = int(input("Ingrese un numero: "))
i = 1
while i<=12:
    print(i,"x",numero,"=",numero*i)
    i += 1

# Solucion Taller1 e3
# posible solucion 1
films = ["wonder woman", "la bella y la bestia", "harry potter", "star wars","superman", "el señor de los anillos"]
PPs = []
for film in films:
    M = int(input("Ingrese la puntuacion de Musica de %s:" % film))
    L = int(input("Ingrese la puntuacion de Libreto de %s:" % film))
    E = int(input("Ingrese la puntuacion de Efectos Espciales de %s:" % film))
    PP = 0.3*L + 0.5*M + 0.2*E
    PPs.append(PP)
puntajeMax = max(PPs)
peliculaConMaxP = films[PPs.index(puntajeMax)]
print("La mejor pelicula es:",peliculaConMaxP)
print("*"*(int(puntajeMax)//2))
# Posible solucion
films = ["wonder woman", "la bella y la bestia", "harry potter", "star wars","superman", "el señor de los anillos"]
puntuacionMax = 0
mejorPeciula = ""
for film in films:
    print("Para",film+":")
    M = int(input("Ingrese la puntuacion de musica de %s:" % film))
    L = int(input("Ingrese la puntuacion de libreta de %s:" % film))
    E = int(input("Ingrese la puntuacion de efectos especiales de %s:" % film))
    PP = 0.3*L + 0.5*M + 0.2*E
    if PP > puntuacionMax:
        puntuacionMax = PP
        mejorPeciula = film
    print(PP)
print("La mejor pelicula es:",mejorPeciula)
print("*"*(int(puntuacionMax)//2))




