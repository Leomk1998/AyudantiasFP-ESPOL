"""
import pandas as pd

df = pd.read_csv("drinks.csv")
#print(df.head(5))
country = df["country"].to_numpy()
dfc = df.to_numpy()
print(dfc)
#print(type(country))
#print(beer)


def crear_matriz(archivo):
    df = pd.read_csv("drinks.txt")
    return df.to_numpy()
"""
"""
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.grid(True, linestyle='-.')
ax.tick_params(labelcolor='r', labelsize='medium', width=3)

plt.show()
"""

#Examen

# Tema 1
"""
a = {2, 8, 14, 19, 20}
b = {14, 16, 20, 4, 2, 1}
c = a.symmetric_difference(b)
resultado = (a - c).union(b - c)
print(resultado)
"""
# Tema 2
"""
import pandas as pd
df = pd.read_csv("especies.csv")
print(df.to_numpy())
"""

"""
def crear_diccionario(archivo, n):
    dicc = {}
    archivo = open(archivo,"r")
    paises = archivo.readline().replace("\n","").split(",")
    lineas = archivo.readlines()
    for linea in lineas:
        lista = linea.replace("\n","").split(",")
        dicc[lista[0]] = []
        for i in range(1,len(lista)):
            if int(lista[i])>n:
                dicc[lista[0]].append((paises[i],int(lista[i])))
    return dicc
dic = crear_diccionario("especies.csv",100)

def mas_popular(dicEspecie, especie):
    paisMax = ""
    maxEjemplares = -1
    for tupla in dicEspecie[especie]:
        if(tupla[1]>maxEjemplares):
            paisMax = tupla[0]
            maxEjemplares = tupla[1]
    return paisMax
#print(dict([("Ecuador",10)]))
#print(mas_popular(dic,"Koala"))

def pais_especie(dicEspecie):
    dicc = {}
    conjuntoPais = set()
    for especie in dicEspecie:
        for tupla in dicEspecie[especie]:
            conjuntoPais.add(tupla[0])
    for pais in conjuntoPais:
        dicc[pais] = []
        for especie in dicEspecie:
            for tupla in dicEspecie[especie]:
                if(tupla[0]==pais and tupla[1]>0):
                    dicc[pais].append(especie)
    return dicc
print(pais_especie(dic))
dicPais = pais_especie(dic)

def especies_en_comun(dicPais, lista_paises):
    conjunto = set(dicPais[lista_paises[0]])
    for pais in lista_paises:
        conjunto = conjunto.intersection(set(dicPais[pais]))
    return tuple(conjunto)
print(especies_en_comun(dicPais,["Australia","Honduras"]))
"""


# Tema 3

import numpy as np
costa = ['Guayaquil','Portoviejo','Manta','Machala']
sierra = ['Quito','Ambato', 'Cuenca','Sto Domingo']
oriente = ['Macas','Tena', 'El Puyo','Zamora']
años = [1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009]
M=np.random.randint(10,1000,size=(len(costa)+len(sierra)+len(oriente),len(años)*2))

# 1    2007
#indice = (años.index(2007)*2)+1 Cap.Hotelera
indice = años.index(2007)*2
v = M[:,indice]
#print(v.sum())

# 2
capHotSierra = M[len(costa):len(costa)+len(sierra),1::2]
# print(M.mean())

# 3



v = np.array([1,3,2,4])
x = v == 2
print(x)
print(v[x])
np.array([randint(1,6),randint(1,6),randint(1,6)])
