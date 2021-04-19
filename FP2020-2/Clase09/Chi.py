def traduccionChi(nombreArchivo):
    archivo = open(nombreArchivo,"r")
    leido = archivo.read()
    listaPalbras = leido.split(" ")
    for i in range(len(listaPalbras)):
        if "chichi" in listaPalbras[i]:
            listaPalbras[i] = listaPalbras[i].replace("chichi", "***")
        if listaPalbras[i].startswith("chi"):
            listaPalbras[i] = "###"+listaPalbras[i][3:]
        if "chi" in listaPalbras[i]:
            listaPalbras[i] = listaPalbras[i].replace("chi", "").replace("***","chi").replace("###","chi")
    print(" ".join(listaPalbras))
traduccionChi("chi.txt")