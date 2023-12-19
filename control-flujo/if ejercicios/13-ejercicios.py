"""
Escribir un programa que pida 2 numeros entero luego deben sumarse y muestre por pantalla si es par o impar.
"""

print("Ingrese números y muestre si es par o impar.")

primer_numero = int(input("Ingrese el primer número: "))
segundo_numero = int(input("Ingrese el segundo número: "))
resultado = primer_numero + segundo_numero

if resultado % 2 == 0:
    print(f"El resultado de la suma es: {resultado} y es par.")
else:
    print(f"El resultado de la suma es: {resultado} y es impar.")
    