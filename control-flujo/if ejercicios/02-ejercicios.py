"""
Determinar si un número es par o impar:
Solicitar al usuario un número e imprimir si es par o impar.
"""
numero = int(input("ingresa un número: "))

if numero % 2 == 0:
    print(f"El número {numero} es par.")

else:
    print(f"El número {numero} es impar.")
