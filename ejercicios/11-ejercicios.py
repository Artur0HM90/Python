"""
If-Else: Desarrolla un programa que solicite al usuario su edad y luego imprima "Eres menor de edad" si la edad es menor o igual a 18, y "Eres mayor de edad" si es mayor a 18.
"""

ingresa_edad = int(input("Ingresa tu edad: "))

if ingresa_edad > 18:
    print(f"Tienes {ingresa_edad} años, Eres mayor de edad.")
else:
    print(f"Tienes {ingresa_edad} años, Eres menor de edad.")