"""
Implementa 2 preguntas donde cada pregunta solo tiene 3 intentos
"""

print("Responde las siguientes preguntas.")

primer_intento = 1
segundo_intento = 1

while primer_intento <= 3:
    print(F"{primer_intento} intento.")
    primer_intento += 1
    print("""Cuantos metros hay en un KILOMETRO
    a: 500 metros.
    b: 350 metros.
    c: 1000 metros.
    d: 2500 metros.
    e: 1400 metros.""")
    primera_respuesta = (str(input("Tú respuesta es: "))).lower()
    if primera_respuesta == "c":
        print("La respuesta fue correcta.")
        break

    else:
        print("La respuesta fue - INCORRECTA intentalo otra vez.")

while segundo_intento <= 3:
    print(f"{segundo_intento} intento.")
    segundo_intento += 1
    print("""Cuantos continentes hay
    a: 5 continentes.
    b: 3 continentes.
    c: 7 continentes.
    d: 9 continentes.
    e: 4 continentes.""")
    segunda_respuesta = (str(input("Tú respuesta es: "))).lower()
    if segunda_respuesta == "a":
        print("La respuesta fue correcta.")
        break
    
    else:
        print("La respuesta fue - INCORRECTA intentalo otra vez.")