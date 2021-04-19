# 23/10/2020
# Ayudante: Leonardo Mendoza

#Ejercicio 1

"""
f = int(input("Escriba un temperatura en grados Farhenheit: "))
c = ((f-32)*5)/9
print("%d grados Farhenheit son %f grados centigrados"%(f,c)) #  %d numeros enteros  %s strings %f numeros decimales
"""

#Ejercicio 2

"""
numero = int(input("Ingrese un numero: "))
mod = numero%2
validacion = mod==0
print("El numero {} es par? {}".format(numero,validacion))
"""

#Ejercicio 3
"""
segundosUsuario = int(input("Ingrese una cantidad de segundos:"))
horas = segundosUsuario//3600
minutos = (segundosUsuario%3600)//60
#minutos = (segundosUsuario-(horas*3600))%60
segundos = segundosUsuario%60
print("%d segundos son %d hora(s), %d minuto(s),%d segundo(s)"%(segundosUsuario,horas,minutos,segundos))
"""
#Ejercicio 4
"""
print("Convetidor de dolares a Euros")
dolares = float(input("Ingrese una cantidad de dolares: "))
valorEuro = 0.885
euros = valorEuro*dolares
print("%.2f dolares son %.2f euros"%(dolares,euros))
"""

#Ejercicio 5
"""
print("Convetidor de euros a dolares")
euros = float(input("Ingrese una cantidad de euros: "))
valorEuro = 0.885
dolares = euros/valorEuro
print("%.2f euros son %.2f dolares"%(euros,dolares))
"""

#Ejercicio 6
"""
print("*******Programa para ver si estas RP******")
par1= int(input("Ingrese su nota de 1par: "))
par2= int(input("Ingrese su nota de 2par: "))
prac= int(input("Ingrese su nota de practica: "))
mej= int(input("Ingrese su nota de mejoramiento: "))
clases= int(input("Ingrese la cantidad de clases: "))
faltas= int(input("Ingrese la cantidad de faltas: "))
promedioTeorico = max((par1+par2)/2,(par1+mej)/2,(mej+par2)/2) # min mean
promedioGeneral = promedioTeorico*0.8 + prac *0.2
porcentajeDeAsistencia = ((clases-faltas)/clases)*100
validacion = promedioGeneral<60 or porcentajeDeAsistencia<60
print("Su promedio general es %.1f y su porcentaje de asistencia es %.1f "%(promedioGeneral,porcentajeDeAsistencia))
print("Reprobado?",validacion)
"""

#Ejercicio 7

#\
"""
print("""
#    Este es un mensaje
#
#        Que usa caracteres especiales
#
#    En un solo print
""")
"""
print("Este es un mensaje \n\n\tQue usa caraccteres especiales \n\nEn un solo print")