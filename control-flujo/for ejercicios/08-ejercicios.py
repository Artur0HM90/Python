"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""

cantidad_invertir = int(input("Ingrese la cantidad a invertir: "))
interes_anual = float(input("Interes anual: "))
años = int(input("años que desea invertir: "))

if cantidad_invertir > 0 and interes_anual > 0 and años > 0:
    for ganancia in range (1, años + 1):       
        interes_ganado = cantidad_invertir * (interes_anual / 100)
        cantidad_invertir += interes_ganado
        print(f"Ganancia del {ganancia} año {round(cantidad_invertir, 2) }")


else:
    print("Ingrese los datos correctos.")