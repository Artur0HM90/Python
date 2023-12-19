"""
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
"""
print("Para saber si debes pagar impuestos requerimos unos datos.")
nombre = str(input("Ingresa tus nombres: "))
edad = int(input("Ingresa tu edad: "))
ingresos = int(input("Ingresa tu ingreso mensual: "))

if edad > 16 and ingresos > 1000:
    print(f"Hola {nombre} tu edad es {edad} tus ingreso mensual es de {ingresos}, tienes que pagar impuestos.")

elif edad <= 16 and ingresos <= 1000:
    print(f"Hola {nombre} tu edad es {edad} tus ingreso mensual es de {ingresos}, no debes pagar impuestos.")
else:
    print("Ingresaste mal uno de los datos.")