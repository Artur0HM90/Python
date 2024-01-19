"""
Nested Loops: Crea un programa que utilice bucles anidados para imprimir un patrón de asteriscos en forma de cuadrado.
"""
numero = int(input("Ingresa un número: "))

for inicio in range(numero):
    for final in range(numero):
        print("* ", end=" ")
    print()