from FuncionesAyudantia4 import *

listaProductos=["Guineos", "Colas", "Carne", "Galletas", "Arroz", "Condimentos", "Lechuga", "Agua Embotellada", "Frejoles"]
stock = [100, 100, 100, 100, 100, 100, 100, 100, 100]
impuesto = ["no paga iva", "paga iva", "no paga iva", "paga iva", "no paga iva", "paga iva", "no paga iva","paga iva","no paga iva"]
precios = [1, 2, 2.5, 0.5, 0.3, 0.2, 0.75, 1, 0.6]
listaCompras = [0,0,0,0,0,0,0,0,0]

print("HOLA, BIENVENIDO A NUESTRA TIENDA")
desea_comprar = input("Desea Comprar? (s/n): ").lower()
while desea_comprar=="s":
    print(listaProductos)
    producto= input("Ingrese un producto que desea comprar o ingrese 'salir': ").title()
    while producto !="Salir":
        cantidad = int(input("Ingrese la cantidad que desea comprar: "))
        if validarStock(producto,cantidad,stock,listaProductos):
            print("Si contramos con esa cantidad de ese producto, se ha agregado en su cuenta.")
            listaCompras[listaProductos.index(producto)]=cantidad
            break
        else:
            print("No contamos con ese stock")
            break
    if producto=="Salir":
        break
print()
print("*************FACTUTA/NOTA DE VENTA**********")
imprimirFactura(listaCompras,listaProductos,precios,impuesto)
