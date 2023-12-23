"""
Solicita al usuario que ingrese números hasta que la suma acumulativa alcance 50.
"""

ingresa_numero = 0

while ingresa_numero <= 50:
    numero = int(input("Ingresa un número: "))
    ingresa_numero += numero
    print(ingresa_numero)