# Cuando queremos recibir información en la consola debemos hacer los siguiente
while True:    
    nombre = input("Ingrese su nombre: ")
    if nombre.isalpha():
        print(nombre)
        break
    else:
        print("Error: Por favor, ingrese un nombre válido que contenga solo letras.")
        print(type(nombre))

edad = int(input("Ingresa su edad: "))
print(edad)
print(type(edad))