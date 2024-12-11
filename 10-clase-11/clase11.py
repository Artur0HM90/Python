# Para crear una lis de forma mas rapida y elegante evitando bucles y condiciones a esto se le llama (comprehesion lists) son breves rapidas y sobre todo potentes. Este nuevo formato de crear listas hace que podamos crearlas utilizando solamente una linea de codigo.

# elevando al cuadrado
squares = [x**2 for x in range(1,11)]
print ("cuadrados:", squares)

# tentereatura a fahrenheit
celsius = [0,10,20,30,40]
fahrenheit = [(temp * 9/5) * 32 for temp in celsius]
print("Temperatura en F: ", fahrenheit)

# numeros pares

numeros = [x for x in range(1,21) if x % 2==0]
print(numeros)

# numeros impares

numeros = [x for x in range(1,21) if x % 2 != 0]
print(numeros)

matrix = [[1,2,3],
        [4,5,6],
        [7,8,9]]

# primera forma comprehesion lists
transpuesta = [[row[i] for row in matrix] for i in range (len(matrix[0]))]
print(matrix)
print(transpuesta)

# segunda otra
transpuesta = []
for i in range (len(matrix[0])):
    transpuesta_row = []
    for row in matrix:
        transpuesta_row.append(row[i])
    transpuesta.append(transpuesta_row)

print(transpuesta)