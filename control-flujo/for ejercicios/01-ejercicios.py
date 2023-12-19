"""
Contador simple:
¿Cómo usar un bucle for para imprimir los números del 1 al número que ingreses?
"""

print("Ingesa de que tabla de multiplicar hasta donde")

tabla_1 = 1
primer_numero = int(input("Ingresa número que quiere multiplicar: "))
segundo_numero = int(input("Ingresa hasta que número quiere que multiplicar: "))

for tabla in range (tabla_1, segundo_numero + 1):
    resultado = tabla * segundo_numero
    print(f"{tabla} x {primer_numero} = {resultado}")

