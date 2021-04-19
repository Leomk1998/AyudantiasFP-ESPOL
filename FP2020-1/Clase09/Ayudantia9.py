#Ayudantia 15/08/2020
#Leonardo Mendoza

from datetime import datetime #Lo usaremos mas adelante

# Ejercicio 1
# Escriba una función que retorne su primer nombre dentro de una tupla.
def primerNombre():
    nombre = "Leonardo"
    return (nombre,)
nombre=primerNombre()
print(nombre)
print(type(nombre))

# Ejercicio 2
#Cree una función que retorne una tupla de la fecha del día de hoy, con el formato (día,mes,año).

def fecha():
    ahora = datetime.now()
    return ahora.day,ahora.month,ahora.year
print(fecha())

# Ejercicio 3
#Cree una función que retorne una tupla de la hora actual, con el formato (hora,minuto,segundo).

def horaActual():
    ahora = datetime.now()
    return ahora.hour,ahora.minute,ahora.second
tuplaHora= horaActual()
print(tuplaHora)
print(type(tuplaHora))

# Ejercicio 4
#Suponga que un profesor tiene dos archivos con las cédulas de los estudiantes de sus cursos
#cada archivo corresponde a un curso (cálculo y álgebra) y se desea saber lo siguiente:


archivoAlgebra = open("algebra.txt","r")
numerosAlgebra = archivoAlgebra.readlines()
for i in range(len(numerosAlgebra)):
    numerosAlgebra[i]=numerosAlgebra[i].replace("\n","").strip()
#print(numerosAlgebra)
archivoAlgebra.close()
archivoCalculo = open("calculo.txt","r")
numerosCalculo = archivoCalculo.readlines()
for i in range(len(numerosCalculo)):
    numerosCalculo[i]=numerosCalculo[i].replace("\n","").strip()
#print(numerosCalculo)
archivoCalculo.close()
conjuntoAlgebra = set(numerosAlgebra)
conjuntoCalculo = set(numerosCalculo)

#Literal 1
# Los estudiantes que forman parte de ambos cursos (seria la interseccion).
# Se hizo de alguno de los cursos, habria que cambiarlo.

#ambosCursos = conjuntoAlgebra | conjuntoCalculo
ambosCursos = conjuntoAlgebra.union(conjuntoCalculo)
print("La union de ambos cursos es:",ambosCursos)

#Literal 2
# Los estudiantes que forman parte del curso de cálculo, y no del curso de álgebra.

#calculoNoAlgebra = conjuntoCalculo - conjuntoAlgebra
calculoNoAlgebra = conjuntoCalculo.difference(conjuntoAlgebra)
algebraNoCalculo = conjuntoAlgebra - conjuntoCalculo
print("Los estudiantes que estan en calculo y no en algebra:",calculoNoAlgebra)
print("Los estudiantes que estan en algebra y no es calculo: ",algebraNoCalculo)

#Literal 3
# Los estudiantes que forman parte del curso de álgebra, y no del curso de cálculo.
#soloCalculoOSoloAlgebra = conjuntoAlgebra.symmetric_difference(conjuntoCalculo)
soloCalculoOSoloAlgebra = conjuntoAlgebra ^ conjuntoCalculo
print(soloCalculoOSoloAlgebra)

#Pregunta
'''
#Producto Cartesiano
import itertools
pc =set(itertools.product(conjuntoCalculo,conjuntoAlgebra))
print(pc)
'''

# Literal 4
# Cree un solo archivo con las cédulas de todos los estudiantes (sin repetir).
archivoSalida = open("literal4.txt","w")
for linea in ambosCursos:
    archivoSalida.write(linea+"\n")
archivoSalida.close()
print("El archivo ha sido creado.")


'''
lista = []
from datetime import datetime
for i in range(1,100,3):
    lista.append((i,i+1,i+2))
print(lista)
conjunto = set([])
conjunto.add(2)
conjunto.add(2)
conjunto.remove(2)
conjunto.discard(2)
print(conjunto)
print(len(conjunto))
'''