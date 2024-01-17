"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
"""
while True:
    print("---> Para ingresar a este local debes ser nayor de edad <---")

    ingrese_edad = int(input("Ingrese su edad: "))

    if ingrese_edad >= 18:
        print(f"Tienes {ingrese_edad} años eres mayor de edad.")

    elif ingrese_edad < 18:
        print(f"Tiuenes {ingrese_edad} años eres menor de edad.")
