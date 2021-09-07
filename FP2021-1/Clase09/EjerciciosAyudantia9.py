"""
import numpy as np

#arr = np.array([[1,2,3],[4,5,6],[4,5,6]],dtype=int)
#print(arr)
#print(arr.shape)
#arr = np.array([1,2,3,4,5,6,7,8,9],dtype=int)
#print(arr)
#mat = arr.reshape(3,3)
#print(mat.shape)
#print(len(mat.shape))
#print(mat)
#print(mat[:,2])

m = np.ones((3,3))
m = np.arange(0,9)
m = m.reshape(3,3)
#m = np.zeros((3,3))
print(m)
"""



# Examen Parcial 2017-1 Tema 2: YouTubers
import numpy as np

españa = ["elrubiusOMG", "VEGETTA777","Pablo Alborán"]
ecuador = ["enchufetvLIVE", "Kreizivoy","Ecuavisa" ]
mexico = ["Yuya", "Werevertumorro", "CaELiKe" ]

M = np.random.randint(500,5000000,size=(4,len(españa)+len(ecuador)+len(mexico)))
print(M)
# Literal 1
"""
rentabilidad = M[3,:]/M[0,:]

rentabilidad_esp = rentabilidad[0:len(españa)]
rentabilidad_ecu = rentabilidad[len(españa):len(españa)+len(ecuador)]
rentabilidad_mex = rentabilidad[len(españa)+len(ecuador):]

maximo_esp = españa[np.argmax(rentabilidad_esp)]
maximo_ecu = ecuador[np.argmax(rentabilidad_ecu)]
maximo_mex = mexico[np.argmax(rentabilidad_mex)]

print(maximo_esp,maximo_ecu,maximo_mex)
"""

#Literal 2
"""
rentabilidad = M[3,:]/M[0,:]
ind = np.argmax(rentabilidad)
youtubers = españa+ecuador+mexico
print(youtubers)
print(youtubers[ind])
if(ind<len(españa)):
    print("España")
elif(ind<len(españa)+len(ecuador)):
    print("Ecuador")
else:
    print("Mexico")
"""
#Literal 3
"""
popularidad_esp = M[0,0:len(españa)]
popularidad_la = M[0,len(españa):]
subs_max_america = np.max(popularidad_la)

filtro = popularidad_esp > subs_max_america
youtubersQueCumplen = np.array(españa)[filtro]
print(youtubersQueCumplen)
print(len(youtubersQueCumplen))
"""
#Literal 4
"""
popularidad = M[0,:]
print(popularidad)
filtro = popularidad>1000000
suscriptoresMas1M = popularidad[filtro]
print(suscriptoresMas1M)
print(np.mean(suscriptoresMas1M))
"""
#Literal 5
rentabilidad_ec = M[3,len(españa):len(españa)+len(ecuador)]/M[0,len(españa):len(españa)+len(ecuador)]
print(rentabilidad_ec)
c1 = 0
c2 = 0
c3 = 0
for rentab in rentabilidad_ec:
    if(0<=rentab<=0.30):
        c1 += 1
    elif (0.31 <= rentab <= 0.60):
        c2 += 1
    elif(rentab>=0.61):
        c3 += 1
respuestal5 = np.array([c1,c2,c3],dtype=int)
print(respuestal5)
