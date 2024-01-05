"""¿La variable 'a' es igual a 5 y la variable 'b' es diferente de 3?"""

print ("Adivina el número mayor.")
print("Ingresa 'a' o la 'b' ")

while True:

    eligue = (str(input("Que vas eleguir a - b: "))).lower()

    if eligue == "a":
        print(f"Eleguiste {eligue} es el número - 5")

    elif eligue == "b":
        print(f"Eleguiste {eligue} es el número - 3")

    else:
        print("Debes eleguir una de las 2 opciones que te dimos.")
        