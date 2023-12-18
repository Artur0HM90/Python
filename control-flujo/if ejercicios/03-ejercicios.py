"""
Comparar dos números:
Pedir al usuario que ingrese dos números e imprimir cuál es el mayor.
"""

primer_numero = float(input("Ingrese el primer número: "))
segundo_numero = float(input("Ingrese el segundo número: "))

if primer_numero > segundo_numero:
    print(f"El primer número es el mayor: {primer_numero}.")

elif primer_numero == segundo_numero:
    print(f"Los dos números son iguales: {primer_numero} - {segundo_numero}.")

else:
    print(f"El segundo número es el mayor: {segundo_numero}.")
