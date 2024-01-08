"""
Crea una función llamada contar_hasta que tome un número como parámetro e imprima los números del 1 hasta ese número utilizando un bucle while.
"""

def contar_hasta():
    inicio = 1
    ingresar_numero = int(input("Ingresa hasta que número se va imprimir: "))
    numeros = []

    while inicio <= ingresar_numero:
        numeros.append (inicio)
        inicio += 1
    return numeros

resultado = contar_hasta()
print(f"Primer número ingresado es: {resultado}")
