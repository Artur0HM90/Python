"""
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
"""

def division (primer_numero, segundo_numero):
    resultado = primer_numero / segundo_numero
    return resultado
primer_numero = int(input("Ingresa primer número: "))
segundo_numero = int(input("Ingresa segundo número: "))
resultado_division = division(primer_numero, segundo_numero)
if resultado_division > 0:
    print(f"El resultado es: {resultado_division}")
else:
    print(f"El resultado es: {resultado_division} - ERROR.")