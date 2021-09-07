# Ayudante: Leonardo Mendoza    04/06/2021

#Ejercicio1

print("*****Validador de Numero de Cedula****")
cedula = input("Ingrese una cedula: ")
val1 = cedula.isdigit()
val2 = len(cedula) == 10 #length
val3 = cedula.startswith("09")
#val3 = cedula[:2] == "09"
val = val1 and val2 and val3
print("¿La cédula",cedula,"es valida?",val)

# Slicing e indexacion

string = "0987654321"
print(string[9]) #indexacion
print(string[3:6]) #slicing


#Ejercicio 2

print("*****Validador de Correos de ESPOL****")
correo = input("Ingrese un correo ESPOL: ")
val1 = correo.endswith("espol.edu.ec")
val2 = correo.count("@")==1
val3 = correo[0].isalpha()
val4 = correo.split("@")[0] != "espol"
#val4 = correo[:correo.index("@")] != "espol"
#print(val4)
val = val1 and val2 and val3 and val4
print("¿El correo",correo,"es valido?",val)

#Ejercicio 3

import random
listaParticipantes = ["Luis","Rafael","Diego","Carlos","Rodrigo","Steven","Jose","Miguel","Luka","Jorge","Mike"]
primerGanador = random.choice(listaParticipantes)
segundoGanador = random.choice(listaParticipantes)
tercerGanador = random.choice(listaParticipantes)
print(primerGanador,"ha ganado una licuadora")
print(segundoGanador,"ha ganado una freidora de aire")
print(tercerGanador,"ha ganado una refrigeradora")

#Ejercicio 4

import random
listaParticipantes = ["Luis","Rafael","Diego","Carlos","Rodrigo","Steven","Jose","Miguel","Luka","Jorge","Mike"]
primero = ganador1 = listaParticipantes.pop(random.randint(0,len(listaParticipantes)-1))
print(primero,"ha salatado en paracaidas")
segundo = listaParticipantes.pop(random.randint(0,len(listaParticipantes)-1))
print(segundo,"ha salatado en paracaidas")
tercero = listaParticipantes.pop(random.randint(0,len(listaParticipantes)-1))
print(tercero,"ha salatado en paracaidas")
print("Lista de personas que se quedaron en el avion",listaParticipantes)

#Ejercicio 5

horaUsuario = input("Ingrese la hora(HH:MM): ") #16:00 21:30 09:30
hora = int(horaUsuario[:horaUsuario.index(":")])
minutos = int(horaUsuario[horaUsuario.index(":")+1:])
if hora<12: # Para AM
    print("%d:%d AM"%(hora,minutos))
elif hora<24: # Para PM # Else if
    print("%d:%d PM"%(hora-12,minutos))
else:
    print("Hora incorrecta")

#Ejercicio 6

print("*****Numero Palindromos*****")
numero = input("Ingrese un numero de cifras impares: ") #100 10000 1000000
val1 = len(numero)%2 != 0
val2 = numero.isdigit()
if(val1 and val2):
    if(numero == numero[::-1]):
        print(numero,"es palindromo.")
    else:
        print(numero,"no es palindromo.")
else:
    print("No está ingresando un número de cifras impares.")
#print("Leonardo"[::2])

#Ejercicio 7
import random
print("*****Juego de los penaltis*****")
posicionUsuario = int(input("Ingrese la posición donde quiere lanzar el penal: "))
posicionPortero = random.randint(1,6)
print("El portero se lanza a",posicionPortero)
if (posicionUsuario >= 1 and posicionUsuario<=6) and (posicionPortero!=posicionUsuario): #GOL
    print("GOOOOOOOOOL")
else:
    if not(posicionUsuario >= 1 and posicionUsuario<=6):
        print("NO ES GOL, tiró fuera")
    elif (posicionPortero==posicionUsuario):
        print("NO ES GOL, arquero la atajo")