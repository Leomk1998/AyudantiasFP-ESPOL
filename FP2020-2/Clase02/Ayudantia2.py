# 30/10/2020
# Ayudante: Leonardo Mendoza

#Ejercicio 1

"""
print("***Validador de cedulas***")
cedula = input("Ingrese su numero de cedula: ")
val1 = cedula.isdigit()
val2 = len(cedula)==10
print(len(cedula))
val3 = cedula.startswith("09")
#val3 = cedula[0:2]=="09"
valfinal = val1 and val2 and val3
print("Su cedula %s es valida?"%(cedula),valfinal)
"""

#Ejercicio 2
"""
print("***Validador de correos espol***")
correo = input("Ingrese su correo espol: ")
val1 = correo.endswith("espol.edu.ec")
val2 = correo.count("@") == 1
val3 = correo[0].isalpha()
#val4 = correo.startswith("espol")
val4 = correo[0:correo.find("@")]!="espol"
#print(correo[0:correo.find("@")])
#if "@" in correo:
#    val4 = correo[0:correo.index("@")]!="espol"
# leoespol.edu.edu.ec
valtotal = val1 and val2 and val3 and val4
print("Su correo espol es valido?",valtotal)
"""

#Ejercicio 4

"""
import random
lista=['Luis','Rafael','Diego','Carlos','Rodrigo','Steven','Jose','Miguel','Luka','Jorge','Mike','Ibai']
print("***Sorteo de electrodomesticos***")
primerGanador = random.choice(lista)
segundoGanador = random.choice(lista)
tercerGanador = random.choice(lista)
print("El primer ganador es %s y ha ganado una licuadora"%primerGanador)
print("El segundo ganador es %s y ha ganado una freidora de aire"%segundoGanador)
print("El tercer ganado es %s y ha ganado una nevera"%tercerGanador)
"""

#Ejercicio 4
"""
import random
lista=['Luis','Rafael','Diego','Carlos','Rodrigo','Steven','Jose','Miguel','Luka','Jorge','Mike','Ibai']
print("***Sorteo de paracaidas***")
print(lista)
primerGanador = lista.pop(random.randint(0,len(lista)-1))
segundoGanador = lista.pop(random.randrange(0,len(lista)))
tercerGanado = lista.pop(random.randint(0,len(lista)-1))
print("El primer ganador es",primerGanador)
print("El segundo ganador es", segundoGanador)
print("El tercer ganado es ", tercerGanado)
print(lista)
"""

#Ejercicio 5
"""
horaUsuario = input("Ingrese la hora en formato 24h(HH:MM):")
hora = int(horaUsuario.split(":")[0])
if hora < 12:
    print("Es AM")
elif hora<24: #else if
    print("Es PM")
else:
    print("Hay un error")
"""
#Ejercicio 6
"""
print("**Programa**")
numero = input("Ingrese un numero de cifras impares: ") # 333 11
val1 = len(numero)%2==1
val2 = numero.isdigit()
if val1 and val2:
    valAlreves = numero==numero[::-1]
    print(numero[::-1])
    print("Es igual al reves y al derecho?",valAlreves)
else:
    print("No ingreso un numero de cifras impares")
"""
#Ejercicio 7
print("***Juego del penal****")
import random
tiroUsuario = int(input("Ingrese un numero: "))
portero = random.randint(1,6)
print("El portero se lanza a %d"%portero)
if (tiroUsuario>=1 and tiroUsuario<=6) and tiroUsuario!=portero:
    print("Es gol")
else:
    print("No es gol")
