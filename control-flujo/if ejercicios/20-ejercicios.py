"""
¿El número ingresado por el usuario es divisible por 2 y 3 simultáneamente?
"""

print("Averigua si el número ingresado es divisible por 2 - 3.")
ingresa_numero = int(input("Ingresa un número positivo: "))

if ingresa_numero >= 0:
    if ingresa_numero % 2 == 0 and ingresa_numero % 3 == 0:
        print(f"El número {ingresa_numero} es divisible por 2 - 3.")
        
        if ingresa_numero % 2 == 0:
            print(f"El número {ingresa_numero} solo es divisible por 2.")

        elif ingresa_numero % 3 == 0:
            print(f"El número {ingresa_numero} solo es divisible por 3.")
else:
    print("Debes ingresr un número.")