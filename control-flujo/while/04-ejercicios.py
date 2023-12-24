"""
Juego de adivinanza con límite de intentos.
Implementa un juego en el que el usuario tiene que adivinar un número secreto usando un bucle while con un límite de intentos.
"""

ingresa_intentos = int(input("Ingresa la cantidad de intentos no debe superar los 10 intentos: "))
limite = 1

if ingresa_intentos <= 10:
    ingrese_numero_para_adivinar = int(input("Ingrese que número van a adivinar: "))
    while limite <= ingresa_intentos:
        intento = float(input(f"Intento {limite} ingrese el número: "))
        limite += 1
        if ingrese_numero_para_adivinar == intento:
            print(f"Adivinaste el número oculto que era {intento} !!!FELICITACIONES¡¡¡")
            break
else:
    print("Debes ingresar un número menor a 11.")