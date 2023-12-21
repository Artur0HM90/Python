"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""

ingrese_numero = int(input("Ingrese un número: "))

if ingrese_numero > 0:
    print (f"Quieres que muestre los números pares o impares? 1. Impares 2. Pares.")
    numero = int(input("Que vas elegir 1 - 2: "))
    if numero == 1:
        print(f"Los números impares desde el 1 hasta el {ingrese_numero} son.")
        for impar in range(ingrese_numero):
            if impar % 2 == 0:
                print(impar + 1)

    elif numero == 2:
        print(f"Los números pares desde el 1 hasta el {ingrese_numero} son.")
        for par in range(ingrese_numero):
            if par % 2 == 0:
                print(par)

else:
    print("Denes ingresar un número positivo y mayor a cero.")