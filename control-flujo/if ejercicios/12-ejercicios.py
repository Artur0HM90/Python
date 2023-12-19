"""
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
"""

print("Ingresaras dos númros.")
primer_numero = int(input("Ingresa el primer número: "))
segundo_numero = int(input("Ingresa el segundo número: "))

if primer_numero > 0 and segundo_numero > 0:
    resultado = primer_numero / segundo_numero
    print(f"la división es: {resultado}")
elif primer_numero > 0 and segundo_numero == 0:
    print("ERROR en la división.")
else:
    print("Debes ingresar números positivos.")