"""
Juego de adivinanza con límite de intentos.
Implementa un juego en el que el usuario tiene que adivinar un número secreto usando un bucle while con un límite de intentos.
"""

limite = 1
numer_adivinar = 50
print ("Adivina el número oculto, tienes 5 intentos.")
while limite <= 5:
    adivinar_numero = int(input(f"Intento {limite} que número es: "))
    limite += 1
    if adivinar_numero == numer_adivinar:
        print(f"Adivinaste el número, era el {numer_adivinar}.")
        break

