"""
Identificar vocal o consonante:
Solicitar al usuario que ingrese una letra y determinar si es una vocal o una consonante.
"""

ingresa_una_letra = input("Ingresa una letra: ")

if ingresa_una_letra.upper() == "A" or ingresa_una_letra.upper() == "E" or ingresa_una_letra.upper() == "I" or ingresa_una_letra.upper() == "O" or ingresa_una_letra.upper() == "U":
    print(f"La letra que ingresaete es una vocal: {ingresa_una_letra.upper()}.")

else:
    print(f"La letra que ingresaste es una consonante: {ingresa_una_letra.upper()}.")
