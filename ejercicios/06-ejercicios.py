"""
Implementa un programa que use un bucle while para imprimir los primeros 5 números pares.
"""
# ahora pediremos un número y debera sacar solo los números paares.
# ahora pediremos al usuario escoger si desea saber número pares o impares.

print("-----------------------------------------")
print("QUE DESEAS SABER NÚMEROS PARES O IMPARES.")
print("-----------------------------------------")
print("1: Pares")
print("2: Impares")

inicio = 0
pares_impares = int(input("Elige 1 - 2: "))

ingresa_numero = int(input("Ingresa un número positivo: "))
if pares_impares == 1:
    print("Elegiste sabeR los números PARES.")
    #inicio = 0
    while inicio < ingresa_numero:
        inicio += 2 
        print(inicio)

elif pares_impares == 2:
    print("Elegiste saber los números IMPARES")
    #inicio = 0
    while inicio < ingresa_numero:
        inicio += 1
        if inicio % 2:
            print(inicio)