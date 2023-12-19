buscar = int(input("Ingresa un número: "))

for numero in range(5):
    print(numero)
    if numero == buscar:
        print("Encontro", buscar)
        break
else:
    print(f"El número {buscar} no se encontra en la lista buscada.")