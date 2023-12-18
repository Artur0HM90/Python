# and - or - not

print("Operador logico AND los dos tienen que se verdaderos")
gas = True
encendido = True

if gas and encendido:
    print("puedes avanzar.")


print("Operador logico OR solo que uno de ellos debe cumplirse")

casa = False
carro = True

if casa or carro:
    print("Puedes descansar")

print("Operador logico NOT cambia el valor si es falso lo va a cambiar a verdadero")

gas = False
encendido = True

if not gas and encendido:
    print("puedes avanzar.")