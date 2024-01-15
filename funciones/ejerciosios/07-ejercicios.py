"""
Escribir una función que calcule el total de una factura tras aplicarle el IGV. La función debe recibir la cantidad sin IGV y el porcentaje de IGV a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IGV, deberá aplicar un 21%.
"""

def con_igv():
    while True:
        print("Bienvenido a la tienda de las ofertas especiales")
        ingresaPrecioTotalParaPagar = int(input("Ingresa el precio: "))
        ingresaCuantoDeIGV = int(input("Ingresa IGV: "))
        if ingresaPrecioTotalParaPagar >= 0 and ingresaCuantoDeIGV >= 0:
            print(f"Precio del producto: {ingresaPrecioTotalParaPagar}")
            print(f"IGV: {ingresaCuantoDeIGV}%")
            sacarIGV = ((ingresaPrecioTotalParaPagar / ingresaCuantoDeIGV) + ingresaPrecioTotalParaPagar)
            precioTotalRedondeado = round(sacarIGV, 2)
            print(f"Total a pagar: {precioTotalRedondeado}")
            print("--------------> Gracias por tu compra <--------------")
                        
        elif ingresaPrecioTotalParaPagar or str(ingresaCuantoDeIGV == ""):
            if ingresaPrecioTotalParaPagar <= 0:
                print(f"Debes ingresar un precio mayor a {ingresaPrecioTotalParaPagar}.")
            
            elif ingresaCuantoDeIGV:
                print(f"Debes ingresar un IGV mayor a {ingresaCuantoDeIGV}.")

            print("-------------------------")

con_igv()