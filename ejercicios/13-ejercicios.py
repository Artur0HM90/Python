"""
Crea una función recursiva para calcular el factorial de un número dado.
"""
ingresa_nunmero = int(input("Ingresa un número: "))
def factorial(ingresa_nunmero): 
    if ingresa_nunmero == 0 or ingresa_nunmero == 1:
        return 1
    else:
        resultado = ingresa_nunmero * factorial(ingresa_nunmero - 1)
        return resultado

resultado = factorial(ingresa_nunmero)
print(f"El factorial de {ingresa_nunmero}! es: {resultado}")