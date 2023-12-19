"""Ejercicios matematicos SUMA - RESTA - MULTIPLICACION - DIVISION                   con la condicional if"""

print("""
Elige que vas a realizar:

1. Suma
2. Resta
3. Multiplicaión
4. División
""")

matematica = int(input("Elige el número: "))

if matematica == 1:
    print("Elegiste la SUMA")
    primer_numero = float(input("Ingresa el primer número: "))
    segundo_numero = float(input("Ingresa el segundo número: "))
    resultado = primer_numero + segundo_numero
    print(f"La suma es: {resultado}")

elif matematica == 2:
    print("Elegiste la RESTA")
    primer_numero = float(input("Ingresa el primer número: "))
    segundo_numero = float(input("Ingresa el segundo número: "))
    resultado = primer_numero - segundo_numero
    print(f"La resta es: {resultado}")

elif matematica == 3:
    print("Elegiste la MULTIPLICACION")
    primer_numero = float(input("Ingresa el primer número: "))
    segundo_numero = float(input("Ingresa el segundo número: "))
    resultado = primer_numero * segundo_numero
    print(f"La multiplicaión es: {resultado}")

elif matematica == 4:
    print("Elegiste la DIVISION")
    primer_numero = float(input("Ingresa el primer número: "))
    segundo_numero = float(input("Ingresa el segundo número: "))
    resultado = primer_numero / segundo_numero
    print(f"La división es: {resultado}")

else:
    print("ERROR - Debes elegir un número de la lista.")