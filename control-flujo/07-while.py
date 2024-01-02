#numero = int(input("Ingresa número: "))
#while numero < 100:
#    print(numero)
    #numero = numero = 2
#    numero *= 2


#comando = ""
#while comando.lower() != "salir":
#    comando = input("$: ")
#    print(comando)

while True:
    print("Ingresa un número entero positivo.")

    ingresa_numero = int(input("Ingresa un número: "))

    if ingresa_numero > 0:
        for par in range (1, ingresa_numero):
            if par % 2 == 0:
                print(f"ingresaste iun par {par}")
    comando = input("Si deseas salir escribe - 'salir' si desea continuar presiona enter: ")
    print(comando)
    if comando.lower() == "salir":
        break