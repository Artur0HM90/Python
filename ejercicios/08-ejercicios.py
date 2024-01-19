"""
Escribe un programa que solicite dos números al usuario y determine si ambos son pares utilizando operadores lógicos.
"""

print("--------------------------------------------")
print("Ingresa dos números para saber si son pares.")
print("--------------------------------------------")

while True:
    def uno(primer_numero):
        if primer_numero % 2 == 0:
            return True
        else:
            False

    def dos(segundo_numero):
        if segundo_numero % 2 == 0:
            return True
        else:
            return False

    def deterninar():
        primer_numero = int(input("Ingresa el primer número: "))
        segundo_numero = int(input("Ingresa el segundo número: "))

        if uno(primer_numero) and dos(segundo_numero):
            print("Los dos número ingresados son PARES.")
            print("------------------------------------")
        else:
            print("Uno de los dos números no es PAR")
            print("--------------------------------")

    deterninar()

            