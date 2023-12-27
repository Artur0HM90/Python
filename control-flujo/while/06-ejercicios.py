"""
Juego de adivinanza con límite de intentos.
Implementa un juego en el que el usuario tiene que adivinar un número secreto usando un bucle while con un límite de intentos.
"""
print("Juego de adivinanza con límite de intentos.")
intentos_primera_pregunta = 1
intentos_segunda_pregunta = 1
while intentos_primera_pregunta <= 5:
    print(f"0{intentos_primera_pregunta} intento.")
    intentos_primera_pregunta += 1
    print("""1. Cuantos continetas existen: 
    a: 8 continentes.
    b: 4 continentes.
    c: 5 continentes.
    d: 3 continentes.
    e: 2 continentes.""")
    pregunta = str(input("Cual es tu respuesta: ")).lower()

    if "c" == pregunta:
        print("Respuesta correcta, felicitaciones.")
        break
    else:
        print("Debes elegir una de las respuestas")
    
while intentos_segunda_pregunta <= 5:
    print(f"0{intentos_segunda_pregunta} intento.")
    intentos_segunda_pregunta += 1
    print("""1. Cuantas ruedas tiene un carro: 
    a: 8 ruedas.
    b: 10 ruedas.
    c: 5 ruedas.
    d: 3 ruedas.
    e: 4 ruedas.""")
    pregunta = str(input("Cual es tu respuesta: ")).lower()

    if "e" == pregunta:
        print("Respuesta correcta, felicitaciones.")
        break
    
    

