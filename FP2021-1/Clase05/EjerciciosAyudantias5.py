# Colecciones

# Listas, tuplas, conjuntos, diccionarios

"""
#Tuplas
a = (1,2,3,4,5)
b = [1,2,3,4,5]
b.append(4)
b.remove(1)
print(b)
"""

# Ejercicio 1

def primerNombre():
    return ("Leonardo",)
nombre = primerNombre()
print(type(nombre))
print(nombre)



# Ejercicio 2

from datetime import *
# from random import randint
def hoy():
    dia = datetime.now().day
    mes = datetime.now().month
    year = datetime.now().year
    return (dia,mes,year)
fecha = hoy()
print(fecha)
print(type(fecha))


# Ejercicios 3

from datetime import *
def hora():
    hora=datetime.now().hour
    minutos=datetime.now().minute
    segundos=datetime.now().second
    return hora, minutos, segundos
hora=hora()
print(hora)

# Ejercicios 4

algebra = '201605224|201908254|201701355|201906055|202106055'
calculo = "201605224|202008254|202101355|201506055|201406055"

listaAlgebra = algebra.split("|")
conjuntoAlgebra = set(listaAlgebra)
listaCalculo = calculo.split("|")
conjuntoCalculo = set(listaCalculo)

# 1 Est de ambos cursos

# ambosCursos = conjuntoAlgebra & conjuntoCalculo # Interseccion
#ambosCursos = conjuntoAlgebra.intersection(conjuntoCalculo)
#print(ambosCursos)

# 2 Calculo si, algebra no

# soloCalculo = conjuntoCalculo - conjuntoAlgebra #  Diferencia
#soloCalculo = conjuntoCalculo.difference(conjuntoAlgebra) #  Diferencia
#soloAlgebra = conjuntoAlgebra.difference(conjuntoCalculo) # No es lo mismo
# A-B != B-A
#print(tuple(soloCalculo))
#print(list(soloAlgebra))
#lista = [1,2,4,5,5,5,5,2,3,5,3,2,1]
#print(list(set(lista)))

# 3
#soloUnCurso = conjuntoAlgebra ^ conjuntoCalculo # DiferenciaSimetrica
#soloUnCurso = conjuntoAlgebra.symmetric_difference(conjuntoCalculo)
#print(soloUnCurso)


# 4
todos = conjuntoCalculo | conjuntoAlgebra   # Union
#todos = conjuntoCalculo.union(conjuntoAlgebra)
#listaTodos = list(todos)
#print(listaTodos)
#print(type(listaTodos))

NOconjuntoVacio = {}
conjuntoVacio = set()
print(NOconjuntoVacio,type(NOconjuntoVacio))
print(conjuntoVacio,type(conjuntoVacio))



# Ejercicio 5

# 3660 1 hora, 1 minuto, 0 segundos
# 1 hora = 3600sg
# 1 minuto = 60sg

def horasMinutosSegundos(segundos):
    horas = segundos//3600
    minutos = (segundos%3600)//60
    segundosRetorno = segundos%60
    return {"horas":horas,"minutos":minutos,"segundos":segundosRetorno} #{clave:valor}
#print(horasMinutosSegundos(7000))

dicc = {"vLuz":300000,"pi":3.141554325423451234,"colecciones":["lista","tuplas","conjuntos","diccionarios"],"diccionarioEs":{"a":1,"b":2}}
print(dicc)


# Ejercicio 6

def crearDiccionario():
    dicc = {}
    nombre = input("Ingrese su nombre:")
    dicc["nombre"] = nombre
    apellido = input("Ingrese su Apellido:")
    dicc.setdefault("apellido",apellido)
    edad = int(input("Ingrese su edad:"))
    dicc["edad"] = edad
    materias = tuple(input("Ingrese el nombre de sus materias (separados por coma): ").split(","))
    dicc["materias"] = materias
    notas = input("Ingrese sus notas (separados por coma): ").split(",")
    for i in range(len(notas)):
        notas[i] = int(notas[i])
    dicc["notas"]= tuple(notas)
    return dicc
dic = crearDiccionario()
#print(dic)
#Ejercicio7
dic["edad"] = dic["edad"]+1
#dic["edad"] += 1
#dic.setdefault("edad",dic["edad"]+1)
dic["nombre"] = "Lionel"
#print(dic)
#Ejercicio8
def consultarNota(diccionario,materia):
    indice = diccionario["materias"].index(materia)
    nota = diccionario["notas"][indice]
    return nota
print(consultarNota(dic,"FP"))


#Taller 2

#Ejercicio 1
# 9782342342342

def validadorISBN():
    ISBN = input("IBSN: ")
    numeros = ISBN[0:12]
    verificador = int(ISBN[12])
    suma = 0
    for i in range(len(numeros)):
        if(i%2==0):
            x=1
        else:
            x=3
        digito = int(numeros[i])
        suma += digito*x
    residuo = suma%10
    if 10-residuo == 10:
        resultado = 0
    else:
        resultado = 10-residuo
    return resultado==verificador
print(validadorISBN())


#Ejercicio 2

def ingresarDatos():
    notas = input("Ingrese sus notas separadas por coma: ").split(",")
    for i in range(len(notas)):
        notas[i] = int(notas[i])
    return notas
def calcularPromedio(notas):
    notasOrdenadas = sorted(notas)
    mejores3notas = notasOrdenadas[::-1][0:3]
    promedio = sum(mejores3notas)/len(mejores3notas)
    return promedio
def asignarNivel(promedio):
    if(promedio>9):
        return "A"
    if (promedio > 8):
        return "B"
    elif (promedio > 7):
        return "C"
    elif (promedio > 6):
        return "D"
    elif (promedio <= 6):
        return "R"

nombre = input("Ingrese su nombre: ")
materia = input("Ingrese su materia: ")
notas = ingresarDatos()
promedio = calcularPromedio(notas)
nivel = asignarNivel(promedio)
print("Nombre:",nombre)
print("materia:",materia)
print("promedio:",promedio)
print("nivel:",nivel)


