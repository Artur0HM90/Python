numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

"""  esta forma es FEO
primero = numeros [0]
segundo = numeros [1]
tercero = numeros [2]
"""

""" segunda forma de hacer
primero, segundo, tercero = numeros
print(primero, segundo, tercero)
"""

""" tercera forma
primero, segundo, *otros = numeros
print(primero, segundo,  otros)
"""

primero, segundo,  *otros,penultimo, ultimo = numeros
print(segundo, penultimo,  otros)
