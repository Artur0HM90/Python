"""
Define una función que tome dos argumentos, los sume y devuelva el resultado. Luego, llama a esa función e imprime el resultado.
"""

def suma (primer_numero, segundo_numero):
    return primer_numero + segundo_numero

def resultado ():
    primer_numero = float(input("Ingresa el primer número: "))
    segundo_numero = float(input("Ingresa el segundo número: "))

    resultado_suma = suma(primer_numero , segundo_numero)
    print (f"el resultado es: {resultado_suma}")

resultado()