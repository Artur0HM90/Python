"""
Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y muestre un mensaje cada vez que un número no sea mayor que el primero.
"""

ingrasar_numeros = int(input("Cuantos números se van ingresar: "))

if ingrasar_numeros > 0:
    primer_numero = int(input("Ingresa el primer número: "))
    if primer_numero > 0:
        for numeros in range (1, primer_numero + 1):
            print(f"{numeros} Escriba un número mayor al primer número {ingrasar_numeros}.")
    
    
else:
    print("Debes ingresar un número positivo o mayor a cero.")