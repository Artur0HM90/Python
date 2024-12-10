frase = input("Ingresa una frase: ")

dividir = frase.split()

contar = {}

for divide in dividir:
    if divide in contar:
        contar[divide] += 1
    else:
        contar[divide] = 1

print(contar)