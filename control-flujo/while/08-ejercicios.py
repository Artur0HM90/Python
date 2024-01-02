"""
Escribe un programa que solicite al usuario ingresar un número entero positivo. Luego, el programa debe contar y mostrar la cantidad de números pares e impares desde 1 hasta el número ingresado, utilizando un bucle for y un bucle while. Asegúrate de incluir instrucciones if para determinar si un número es par o impar.
"""

print("Determinar si un número es par o impar.")

while True:
    numero = int(input("Ingresa un número: "))
    print(f"""ingresaste el {numero} quieres saber los números pares o los impares 
    1. Paras 
    2. Impares""")
    par_impar = int(input("Que vas elegir: "))

    if par_impar == 1:
        print(f"Elegiste averiguar los números pares del {numero}.")
        for par in range (numero):
            if par % 2 == 0:
                print (par) 

    elif par_impar == 2:
        print(f"Elegiste averiguar los números impares del {numero}.")
        for impar in range (numero):
            if impar % 2 == 0:
                print (impar + 1)

    salir = (str(input("Si desea salir escriba - 'salir' - si desea continuar presione enter: "))).lower()
    print (salir)
    if salir == "salir":
        break
