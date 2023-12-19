"""
Ejercicio 1
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
"""

print("Inresaras la edad para ver si es mayor de edad.")

edad = int(input("Ingresa edad: "))

if edad >= 18:
    print(f"Tienes {edad} años, eres mayor de edad.")

elif edad < 18:
    print(f"Tienes {edad} años, eres menor de edad.")

else:
    print ("Debes ingresar un número.")