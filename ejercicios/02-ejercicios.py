"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
"""

print("----------------------------------------------")
print("---> Bienvenidos a tu Banco que te cuida. <---")
print("----------------------------------------------")

print("Deseas crear una cuenta bancaria en nuestra institución")
inscripcion = (str(input("""
1: Si
2: No
que vas elgir / escribe Si - No: """))).lower()

if inscripcion == "si" or inscripcion == "s":
    print("Gracias por elegir nuestra entidad.")
    while True:
        print("Debes crear una contraseña de 6 digitos.")   
        crear_tu_contrasena = input("Ingresa una contraseña: ")
        if len(crear_tu_contrasena) == 6 and crear_tu_contrasena.isdigit():
            print("Creaste una contraseña")
            consulta_si_va_realizar_deposito_inicial = (str(input("Vas a depositar un monto / Si - No: "))).lower()
            if consulta_si_va_realizar_deposito_inicial == "si":
                cantidad_del_deposito_inicial = float(input("Que cantidad vas a depositar: "))
                print("------------------------------")
                print(f"Depositaste: S/{cantidad_del_deposito_inicial}. ")
                print("------------------------------")
                print("Gracias por su confianza en nuestro Banco.")
            else:
                print("Gracias por elegir nuestra institucion.")
            break
        else:
            print("--------------------------------------")
            print("-- ERROR - Debes ingresar 6 numeros --")
            print("--------------------------------------")
else:
    print("Lo esperamos la proxima.")

print("Bienvenido a nuestro banco.")
print("------------------------------------------- ")
ingresar = (str(input("Deseas ingresar ver a tu cuenta - Si / No: "))).lower()
print("------------------------------------------- ")
if ingresar == "si" or ingresar == "s":
    inicio = 1
    print("Tienes 3 intentos para ingresar a tu cuenta.")
    while inicio <= 3:
        print("--------------------------")
        print(f"{inicio} intento.")
        inicio += 1
        ingresa_tu_contrasena = int(input("Ingresa tu contraseña: "))
        if crear_tu_contrasena == ingresa_tu_contrasena:
            print(f"bienvenido {cantidad_del_deposito_inicial}")
            break
    else:
        print("Has agotado tus 3 intentos")
else:
    print("Te esperamos para tu proximo retiro.")