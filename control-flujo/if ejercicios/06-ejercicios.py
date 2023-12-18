"""
Determinar si un año es bisiesto:
Pedir al usuario que ingrese un año e imprimir si es bisiesto o no. Un año es bisiesto si es divisible por 4, pero no por 100, a menos que también sea divisible por 400.
"""

bisiesto = int(input("Ingresa año: "))

if bisiesto % 4 == 0:
    print(f"El año: {bisiesto} es bisiesto.")

else:
    print(f"El año: {bisiesto} no es bisiesto.")