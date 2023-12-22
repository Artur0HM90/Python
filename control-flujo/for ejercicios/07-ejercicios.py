"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
"""

numero_entero = int(input("Ingrese un número: "))
for retro in range(numero_entero, -1, -1):
    print(retro, end=", " )
    