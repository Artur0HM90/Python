"""
Escribir un programa que pregunte al usuario su nombre y su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""

ingrese_nombre = str(input("Ingrese su nombre: "))
ingrese_edad = int(input("Ingrese su edad: "))

print(f"Beinvenido {ingrese_nombre}.")
for edad in  range (ingrese_edad):
    print(f"{edad + 1}")