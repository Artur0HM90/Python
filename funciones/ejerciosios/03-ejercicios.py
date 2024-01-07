"""
Calculadora básica:
Crea una calculadora simple usando funciones. La calculadora debe ser capaz de realizar operaciones de suma, resta, multiplicación y división. Define funciones separadas para cada operación.
"""

while True:
    def suma(primer_numero, segundo_numero):
        return primer_numero + segundo_numero   # me falto el return

    def resta(primer_numero, segundo_numero):
        return primer_numero - segundo_numero

    def multiplicacion(primer_numero, segundo_numero):
        return primer_numero * segundo_numero

    def division(primer_numero, segundo_numero):
        if segundo_numero != 0:
            return primer_numero / segundo_numero
        else:
            return ("No puedes dividir entre cero.")



    def calculadora():
        print("Calculadora basica.")
        print("1: SUMA")
        print("2: RESTA")
        print("3: MULTIPLICACIÓN")
        print("4: DIVISIÓN")
        elegir = int(input("Que vas elegir - 1/2/3/4: "))

        primer_numero = float(input("Ingresa el primer número: "))
        segundo_numero = float(input("Ingresa el segundo número: "))

        if elegir == 1:
            print("Elegiste la SUMA.")
            resultado = suma(primer_numero, segundo_numero)
            print(f"El resultado de {primer_numero} + {segundo_numero} = {resultado}")
        
        elif elegir == 2:
            print("Elegiste la RESTA.")
            resultado = resta(primer_numero, segundo_numero)
            print(f"El resultado de {primer_numero} - {segundo_numero} = {resultado}")

        elif elegir == 3:
            print("Elegiste la MULTIPLICACIÓN.")
            resultado = multiplicacion(primer_numero, segundo_numero)
            print(f"El resultado de {primer_numero} x {segundo_numero} = {resultado}")
        
        elif elegir == 4:
            print("Elegiste la DIVISIÓN.")
            resultado = division(primer_numero, segundo_numero)
            print(f"El resultado es {primer_numero} / {segundo_numero} = {resultado}")


    calculadora()
    print("--------------------------")



