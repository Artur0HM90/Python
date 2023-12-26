"""
Realiza un pequeño sistema de banco donde te pida lo siguiente:
1. Te pida un usuario y contraseña para el registro en el bacno. --- listo
2. Que te pida la contraseña y el usuario para el ingreso a su cuenta -- listo
3. Si ingresa 3 veces mal la contraseña o el usuario te imprima un mensaje que diga ingreso mal la contraseña o el usuario --listo
4. Si ingresa bien el usuario y contrasela imprima un mensaje que diga ingresaste a tu cuenta --listo
5. Ingresado a tu cuenta debes ingresar un monto de 1100. --listo
"""

ingresa_usuario_crear_cuenta = str(input("Ingresa un usuario para crear tu cuenta: "))
ingresa_contraseña_crear_cuenta = int(input("Ingresa una cantraseña para crear tu cuenta: "))
limite_de_intentos = 1

while limite_de_intentos <= 3:
    print(f"intento {limite_de_intentos}")
    limite_de_intentos += 1
    ingresar_usuario = str(input("Ingresa tu usuario: "))
    ingresar_contrasena = int(input("Ingresa tu contraseña: "))
    if ingresa_usuario_crear_cuenta.lower() == ingresar_usuario.lower() and ingresa_contraseña_crear_cuenta == ingresar_contrasena:
        print("Ingresaste a tu cuenta bancaria.")
        ingreso_de_dinero = int(input("Cuanto va depositar: "))
        print(f"{ingresa_usuario_crear_cuenta.lower()} en tu cuenta bancaria tienes en total: ${ingreso_de_dinero}")
        break

    else:
        print("ERROR - ingresaste mal uno de los dos datos, intente otra vez.")