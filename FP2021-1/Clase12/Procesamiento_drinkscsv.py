#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df = pd.read_csv("drinks.csv")


# In[5]:


df.head()


# In[7]:


type(df["beer_servings"])
#Cuando tomo un registro como serie, ese registro tiene los mismos campos que el DF
#Los registros de columnas son dataframe


# In[20]:


#Seleccionar Data    Filtrar datos con indexamiento booleano
#Cuanto paises consumen cero Alcohol?
#Solo la condicion
#print((df["total_litres_of_pure_alcohol"]==0).sum())


# In[23]:


#Dataframe filtrado para responder otras preguntas
df2 = df[df["total_litres_of_pure_alcohol"]==0]
#print(df2)

# In[28]:


#Cuantos paises consumen cero alcohol?
df2.shape
rows,cols=df2.shape
rows


# In[29]:


#Determine en que contienente estan esos paises
df2["continent"].unique()


# In[33]:


df3 = df[df["beer_servings"]> df["wine_servings"] ]
df3.head()


# In[40]:


#Encontrar el indice del registro con mas alto valor en una columna dada
#idxmax devuelve el indice del registro
#Cual es el pais con mas alto consumo de cerveza?
indice = df["beer_servings"].idxmax()
row_max_beer = df.iloc[indice]
row_max_beer


# In[41]:


type(row_max_beer)


# In[42]:


row_max_beer["country"]  #Aqui recien respondo la pregunta de cual es el valor







