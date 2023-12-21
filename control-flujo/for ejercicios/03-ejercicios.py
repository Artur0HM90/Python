"""
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces
"""

ingrese_palabra = str(input("Ingrese una palabra: "))
ingrese_cantidad = int(input(f"Ingrese la cantidad que se repetira la palabra {ingrese_palabra}: "))

for palabra in range (ingrese_cantidad):
    print(f"{palabra + 1 } { ingrese_palabra}.")