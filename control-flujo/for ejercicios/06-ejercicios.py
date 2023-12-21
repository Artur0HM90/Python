"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""

ingrese_numero = int(input("Ingres un número: "))

if ingrese_numero > 0:
    print("Que deseas averiguar números 1. Pares o 2. Impares")
    pares_impares = int(input("Que vas elegir 1 - 2 : "))
    if pares_impares == 1:
        print(f"Elegiste números pares desde el 1 al {ingrese_numero}.")
        for par in range (ingrese_numero):
            if par % 2 == 0:
                print (par)
    elif pares_impares == 2:
        print(f"Elegiste números impares desde el 1 al {ingrese_numero}.")
        for impar in range (ingrese_numero):
            if impar % 2 == 0:
                print(impar + 1)
else:
    print("Debes ingresar un número psitivo y mayor a cero")