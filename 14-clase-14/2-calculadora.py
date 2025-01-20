def calcualdora(primerNumero, segundoNumero, operacion):
    if operacion == "suma":
        return primerNumero + segundoNumero
    elif operacion == "resta":
        return primerNumero - segundoNumero
    elif operacion == "multiplicacion":
        return primerNumero * segundoNumero
    elif operacion == "division":
        if segundoNumero == 0:
            return "NO SE PUEDE DIVIDIR"
        else:
            return primerNumero / segundoNumero
    else:
        return "Operación no valida"
    
opcion = """QUE VAS ELEGIR: 
---------------
1. SUMA
2. RESTA
3. MULTIPLICACIÓN
4. DIVISIÓN
"""
print(opcion)

try:
    elegir = int(input("Elige entre 1 - 4: ")) 
    if elegir not in [1,2,3,4]:
        raise ValueError("Opción fuera de rango.")
    
    numero_uno = float(input("Ingresa el primer número: "))
    numero_dos = float(input("Ingresa el segundo número: "))

    operaciones = {
        1: "suma",
        2: "resta",
        3: "multiplicación",
        4: "división"
    }

    resultado = calcualdora(numero_uno, numero_dos, operaciones[elegir])
    print(f"El resultado es: {resultado}")

except ValueError as e:
    print(f"Error: {e}")

except Exception as e:
    print(f"Error inesperado: {e}")