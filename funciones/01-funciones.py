nombres = str(input("Ingresa tus Nombres: "))
apellidos = str(input("Ingresa tus apellidos: "))

def hola(nombres, apellidos="Sin datos"):
    print("Hola Mundo!")
    print(f"Bienvenido {nombres} {apellidos}")

hola(nombres.capitalize() )


hola(apellidos, nombres)