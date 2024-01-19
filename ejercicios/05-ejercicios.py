"""
Crea un programa que solicite al usuario ingresar un número y luego imprima "Es positivo" si el número es mayor que 0, y "Es negativo" si es menor o igual a 0.
"""
while True:
    ingresa_numero = float(input("Ingresa un número: "))

    if ingresa_numero > 0:
        print(f"El número {ingresa_numero} ES POSITIVO.")
        print("-------------------------------<")

    else:
        print(f"El número {ingresa_numero} ES NEGATIVO.")
        print("-------------------------------<")
