"""
Calculadora básica:
Crea una calculadora simple usando funciones. La calculadora debe ser capaz de realizar operaciones de suma, resta, multiplicación y división. Define funciones separadas para cada operación.
"""
while True:
    def suma (primer_numero, segundo_numero):
        return primer_numero + segundo_numero

    def resta (primer_numero, segundo_numero):
        return primer_numero - segundo_numero

    def multiplicación (primer_numero, segundo_numero):
        return primer_numero * segundo_numero

    def division (primer_numero, segundo_numero):
        if segundo_numero != 0:
            return primer_numero / segundo_numero
        else:
            return "ERROR - División por cero."
        
    def desarrollo ():
        print ("Calculadora basica - que vas elige.")
        print("1: SUMA")
        print("2: RESTA")
        print("3: MULTIPLICACIÓN")
        print("4: DIVISIÓN")

        opcion = int(input("Cual vas elegir 1/2/3/4: " ))

        primer_numero = float(input("Ingresa primer número: "))
        segundo_numero = float(input("Ingresa segundo número: "))

        if opcion == 1:
            print("Elegiste la SUMA.")
            resultado = suma(primer_numero,segundo_numero)

        elif opcion == 2:
            print("Elegisate la RESTA.")
            resultado = resta(primer_numero,segundo_numero)
        
        elif opcion == 3:
            print("Elegiste la MULTIPLICAIÓN.")
            resultado = multiplicación(primer_numero,segundo_numero)

        elif opcion == 4:
            print("Elegiaste la DIVISIÓN.")
            resultado = division(primer_numero,segundo_numero)
        
        print(f"---> El resultado es: {resultado}")
    desarrollo()
    print("-------------------------")
