"""
Validar contraseña:
Solicitar al usuario que ingrese una contraseña. Si la contraseña es "secreta", imprimir un mensaje de acceso permitido; de lo contrario, imprimir un mensaje de acceso denegado.
"""

contraseña = int(input("Ingrese una contraseña para crear su usuario: "))

print("Para ingresar a su cuenta debe ingresar la contraseña correcta.")

validar_contraseña = int(input("Ingrese su contraseña: "))

if contraseña == validar_contraseña:
    print("Su contraseña es valida tiene el acceso permitido.")

else:
    print("Su contraseña es incorrecta acceso denegado.")
