"""
"¿Cómo implementarías en un programa la condición para aplicar un descuento del 10% si el cliente ha comprado más de 5 productos? Utiliza estructuras de control como if, for, o while según sea necesario."
"""

print("Bienvenido a la tiende de las ofertas.")
producto_para_descuento = 5
descuento = 10

while True:
    compras = int(input("Cuantos productos vas a comprar: "))
    if compras >= producto_para_descuento:
        print(f"Compraste {compras} productos. Te corresponde un descuento del {descuento}%.")
        break
    
    elif compras < producto_para_descuento:
        desea_comprar_mas = producto_para_descuento - compras
        if desea_comprar_mas >= 2:
            print(f"Compraste {compras} productos. Te falta {desea_comprar_mas} productos para su descuento del {descuento}%.")
            desea_comprar_mas_productos = (str(input("Desea comprar más productos: si - no: "))).lower()
            if desea_comprar_mas_productos == "si":
                compras_adicionales = int(input("Cuantos productos adicionales vas a comprar: "))
                total_de_tus_compras = compras + compras_adicionales
                print (f"Total de productos comprados es {total_de_tus_compras}, te corresponde del {descuento}%. ")
            else:
                print(f"Total de productos comprados es {compras}.")
            break

        elif desea_comprar_mas == 1:
            print(f"Compraste {compras} productos. Te falta {desea_comprar_mas} producto para su descuento del {descuento}%.")
            desea_comprar_mas_productos = (str(input("Desea comprar más productos: si - no: "))).lower()
            if desea_comprar_mas_productos == "si":
                compras_adicionales = int(input("Cuantos productos adicionales vas a comprar: "))
                total_de_tus_compras = compras + compras_adicionales
                print (f"Total de productos comprados es {total_de_tus_compras}, te corresponde del {descuento}%. ")
            else:
                print(f"Total de productos comprados es {compras}.")
            break