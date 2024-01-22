"""
Manejo de Listas/Arrays: 
Implementa un programa que tome una lista de números y devuelva la suma de los números pares en la lista.
"""

cuantos_numeros_vas_ingresar = int(input("Ingresa la cantidad de números que vas ingresar: "))
inicio = 0

while inicio <= cuantos_numeros_vas_ingresar:
    inicio += 1
    ingresa_numeros = int(input(f"Ingresa el {inicio} número: "))

    for suma in ingresa_numeros:
        if suma % 2 == 0:
            inicio += suma
            print (f"La suma es: {suma}.")