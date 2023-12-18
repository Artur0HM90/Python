"""Verificar si un número es positivo o negativo: 
Pedir al usuario que ingrese un número e imprimir si es positivo, negativo o cero."""

numero = float(input("Ingrese un número: "))

if numero > 0:
    print(f"El número {numero} es positivo.")

elif numero == 0:
    print(f"Ingresaste el {numero}.")

else:
    print(f"El número {numero} es negativo.")
