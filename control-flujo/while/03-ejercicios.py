"""
Muestra la tabla de multiplicar del 3 utilizando un bucle while.
"""

tabla = 1
ingresa_numero = int(input("Ingresa un númmero: "))

if ingresa_numero >= 0:
    while tabla <= 12:
        print(f"{tabla} x {ingresa_numero} = {tabla * ingresa_numero}")
        tabla += 1
else:
    print("Debes ingresar un número mayor a cero.")