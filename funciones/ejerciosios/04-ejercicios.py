"""
Escribe una función llamada verificar_numero que tome un argumento (número) y devuelva "Es positivo" si el número es mayor que 0, "Es negativo" si es menor que 0, y "Es cero" si es igual a 0.
"""
def verificar_numero():
    ingresar_numero = int(input("Ingresa un número: "))

    if ingresar_numero > 0:
        return (f"El número ingresado es {ingresar_numero} positivo.")

    elif ingresar_numero < 0:
        return (f"El número ingresado es {ingresar_numero} es negativo.")
                
    elif ingresar_numero == 0:
        return (f"El número ingresado es {ingresar_numero} es igual a cero.")
        
    else:    
        return ("ERROR - Debes ingresar un número.")

resultado = verificar_numero()
print(resultado)