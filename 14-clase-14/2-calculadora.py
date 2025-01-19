def suma(primer_numero, segundo_numero):
    return primer_numero + segundo_numero

def resta(primer_numero, segundo_numero):
    return primer_numero - segundo_numero

def multiplicacion(primer_numero, segundo_numero):
    return primer_numero * segundo_numero

def division(primer_numero, segundo_numero):
    if segundo_numero == 0:
        print("NO SE PUEDE DIVIDIR.")
    else:
        return primer_numero / segundo_numero

opcion = """QUE VAS ELEGIR: 
---------------
1. SUMA
2. RESTA
3. MULTIPLICACIÓN
4. DIVISIÓN
"""
print(opcion)
elegir = int(input("Elige entre 1 - 4: ")) 

numero_uno = float(input("Ingresa el primer número: "))
numero_dos = float(input("Ingresa el segundo número: "))

match elegir:
    case 1: 
        resultado = suma(numero_uno, numero_dos)
    case 2:
        resultado = resta(numero_uno, numero_dos)
    case 3:
        resultado = multiplicacion(numero_uno, numero_dos)
    case 4:
        resultado = division(numero_uno, numero_dos)

print(f"El resulta es {resultado}")