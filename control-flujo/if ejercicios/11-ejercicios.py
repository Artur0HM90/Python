"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
"""

print("Para ingresar a nuestra plataforma debes registrarte SI o NO")
registrarse = str(input("Que eliges: "))

if registrarse == "si" or registrarse == "SI" or registrarse == "s" or registrarse == "S":
    registrarse_contraseña = int(input("Registre su contraseña: "))
    print("Graciaspor ingresar su contraeña.")
    ingrese_contraeña = int(input("Ingrese su contraseña: "))
    if registrarse_contraseña == ingrese_contraeña:
        print("Su contraseña es correcta.")
    else:
        print("Contraseña incorrecta.")

elif registrarse == "no" or registrarse == "NO" or registrarse == "n" or registrarse == "N":
    print("Entendemos lo esperamos la proxima vez. GRACIAS.")


else:
    print("ERROR - Ingresoun valor equivocado")