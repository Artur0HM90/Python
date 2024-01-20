"""
While Loop con Condiciones: 
Escribe un programa que simule un juego en el que el usuario debe adivinar un número secreto. Utiliza un bucle while para permitir múltiples intentos y proporciona pistas al usuario.
"""
import math

print("------------------------")
print("Adivina el número oculto")
print("------------------------")
numero_oculto = 25

while True:
    try:
        ingresa_numero = int(input("Ingresa un número: "))
        if numero_oculto == ingresa_numero:
            print("----------------------------------")
            print(f"Adivinaste {ingresa_numero} es el número oculto.")
            print("----------------------------------")

            break

        else:
            resultado = abs(numero_oculto - ingresa_numero)
            if resultado <= 6:
                print("Estas muy cerca. sigue intentando...")
            
            elif resultado <= 11:
                print("Estas muy cerca. Sigue intentando...")
            
            else:
                print("Estas muy lejos. Sigue intentanto...")

    except ValueError:
        print("Debes ingresar un número. Intentalo otra vez")



