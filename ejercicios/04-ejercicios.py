"""
Escribe un programa en cualquier lenguaje de programación que utilice un bucle for para imprimir los números del 1 al 5.
"""
# Ahora vamos a intentar mejorar la pregunta vamos a pedir un número y se va tener que imprimir hasta ese número

primer_numero = int(input("Ingresa un número positivo: "))
for numeros in range (1, primer_numero):
    print(numeros + 1)