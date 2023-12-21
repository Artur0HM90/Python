buscar = 35
for numero in range (5):
    print(numero)
    if numero == buscar:
        print("Encontrado", buscar)
        break
else:
    print(f"No se encontro el número {buscar} buscado.")

for char in "Clandestino":
    print(char)