"""
¿Cómo puedes definir una función en Python que acepte dos argumentos (por ejemplo, 'a' y 'b') y devuelva la suma de ambos?
"""
primer_numero = int(input("Ingresa primer número: "))
segundo_numero = int(input("Ingresa segundo número: "))

def suma (primer_numero,segundo_numero):
    resultado = primer_numero + segundo_numero
    return resultado

operacion = suma(primer_numero, segundo_numero)

print(f"El resultado de la suma es: {operacion}")
