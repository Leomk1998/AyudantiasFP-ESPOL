españa = ["elrubiusOMG", "VEGETTA777","Pablo Alborán"]
ecuador = ["enchufetvLIVE", "Kreizivoy","Ecuavisa" ]
mexico = ["Yuya", "Werevertumorro", "CaELiKe" ]
youtubers = españa+ecuador+mexico
#print(youtubers)

import numpy as np
M = np.random.randint(500,5000000,size=(4,len(youtubers)))
#print(M)

# Literal1
youtubersMayorRent = []
rentabilidad = M[3,:] / M[0,:] # M[filas,columnas]
renta_es = rentabilidad[0:len(españa)]
renta_ec = rentabilidad[len(españa):len(españa)+len(ecuador)]
renta_mx = rentabilidad[len(españa)+len(ecuador):]
youtubersMayorRent.append(españa[np.argmax(renta_es)])
youtubersMayorRent.append(ecuador[np.argmax(renta_ec)])
youtubersMayorRent.append(mexico[np.argmax(renta_mx)])
#print(youtubersMayorRent)
# Literal2
indice = np.argmax(rentabilidad)
youtuberMasRentabilidad = youtubers[indice]
#print(youtuberMasRentabilidad)
# Literal3
SubsYoutuberMPA = np.max(M[0,len(españa):])
filtro = M[0,:len(españa)] > SubsYoutuberMPA
ayoutubersEspMasA = np.array(españa,str)[filtro]
literal3 = len(ayoutubersEspMasA)
#print(literal3)
# Literal4
filtro = M[0,:] > 1000000
promedio = int(np.mean(M[1,:][filtro]))
#print(promedio)
# Literal5
filtroC1 = renta_ec<=0.3
filtroC2 = (renta_ec>0.3) & (renta_ec<=0.6)
filtroC3 = renta_ec>0.6
nc1 = len(renta_ec[filtroC1])
nc2 = len(renta_ec[filtroC2])
nc3 = len(renta_ec[filtroC3])
arreglol5 = np.array([[1,2,3],[nc1,nc2,nc3]])
#print(arreglol5)
# Literal6
ganancias_es = np.sum(M[3,:len(españa)])
ganancias_ec = np.sum(M[3,len(españa):len(españa)+len(ecuador)])
ganancias_mx = np.sum(M[3,len(españa)+len(ecuador):])
listaGanancias = [ganancias_es,ganancias_ec,ganancias_mx]
listaPaises = ["España","Ecuador","Mexico"]
indmax = listaGanancias.index(max(listaGanancias))
indmin = listaGanancias.index(min(listaGanancias))
porcentaje = ((listaGanancias[indmax] - listaGanancias[indmin]) / listaGanancias[indmin]) * 100
#print(listaPaises[indmax],"generó","%.2f"%porcentaje,"% más de ganancias que",listaPaises[indmin])
