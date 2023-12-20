"""
Escriba un programa que pida dos números y que conteste cuál es el menor y cuál el mayor o que escriba que son iguales.
"""

primer_numero = int(input("Ingrese el primer número: "))
segundo_numero = int(input("Ingrese el segundo número: "))

if primer_numero > segundo_numero:
    print(f"El primer número es mayor {primer_numero} el segundo es el menor {segundo_numero}")

elif segundo_numero > primer_numero:
    print(f"El segundo número es mayor {segundo_numero} el primer es el menor {primer_numero}")

elif primer_numero == segundo_numero:
    print(f"Los dos números son iguales {primer_numero} - {segundo_numero}")

else:
    print("Error debes ingresar números.")