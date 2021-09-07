

#Ayudantia1

# Ejercicio 1
#f = 78
"""
f = int(input("Escriba la temperatura: "))
c = int(((f-32)*5)/9)
print("%d grados Farenheit son %d grados celcius"%(f,c))
print("{} grados Farenheit son {:.2f} grados celcius".format(f,c))
"""
# Ejercicio 2
"""
numero = int(input("Ingrese un numero: "))
val = (numero%2) == 0
print("Su numero es par?",val)
"""
#Ejercicio 3
"""
inversion = float(input("Cuanto desea invertir?"))
interes = int(input("Tasa de interes: "))
years = int(input("Numero de años: "))
cf = inversion*((1+(interes/100))**years)
print("El capital final es:", cf)
"""
# Ejercicio 4
# 7260 1 hora, 1 minuto, 5 segundo
"""
segundosUsuario = int(input("Ingrese una cantidad de segundos: "))
horas = segundosUsuario//3600
minutos = (segundosUsuario%3600)//60
segundos = (segundosUsuario%60)
print("%d segundos son %d horas, %d minutos y %d segundos"%(segundosUsuario,horas,minutos,segundos))
"""
# Ejercicio 5
"""
valorDolar = float(input("Ingrese una cantidad en dolares: "))
valorEuro = (0.885)*valorDolar
print("{} dolares son {} euros".format(valorDolar,valorEuro))
"""
# Ejercicio 6
"""
valorE = float(input("Ingrese una cantidad en euros: "))
valorD = valorE/(0.885)
print("{:.2f} euros son {:.2f} dolares".format(valorE,valorD))
print("%.2f euros son %.2f dolares"%(valorE,valorD))
print(valorE,"euros son",round(valorD,2),"dolares")
"""
# Ejercicio 7
"""
parcial1 = int(input("Ingrese su nota de primer parcial: "))
parcial2 = int(input("Ingrese su nota de segundo parcial: "))
mej = int(input("Ingrese su nota de mejoramiento: "))
notaPractica = int(input("Ingrese su nota practica: "))
clasesAsistidas = int(input("Ingrese la cantidad de clases a las que asistio: "))
totalClases = int(input("Ingreses de cantidad total de clases: "))
notalFinal = max((parcial1+parcial2)/2,(parcial1+mej)/2,(mej+parcial2)/2)
print(notalFinal)
porcAsistencia = clasesAsistidas/totalClases
aprobo = ((notalFinal*0.8 + notaPractica*0.2) >= 60) and (porcAsistencia>=0.6)
print("Usted aprobo?",aprobo)


print(max(1,5,-10,2,4,3))
print(min(1,5,-10))
"""

# Ejercicio 8

#print("""Este es un mensaje

#        Que usa caracteres especiales
        
#En un solo string
#""")

#print('Este es un mensaje \n\n \t\tQue usa caracteres especiales \' "HOLA"\n\n En un solo string')

# Ejercicio 2 Participacion

dineroClienteDA = 40
valorProductoDC = 41.27
tasaCambio = 0.72
# cambio = dineroClienteDA - valorProductoDC*tasaCambio
valorProductoDA = valorProductoDC*tasaCambio
cambio = dineroClienteDA-valorProductoDA
print("%.2f"%cambio)

