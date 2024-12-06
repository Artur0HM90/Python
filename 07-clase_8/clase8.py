# clase lista

to_do = ["Dirigirnos al hotel",
        "Ir a almorzar",
        "Visitar al museo",
        "Volver al hotel"]
print(to_do)

numbers = [1,2,3,4, "cinco"] 
print(type(numbers)) # sera reconocido como una class lista

mix = ["uno", 2, 3.14, True, [1,2,3]]
print(mix)
print(type(mix))



print(len(mix)) # tambien podermos contar cuantos datos tenemos almacenoados usaremos LEN
print("Primer elemento", mix[0]) # tambien podemos usar la indexacion con usaremos[]
print("Segundo elemento", mix[1])
print("Ultimo elemento", mix[-1])

# podemos extraer porciones de datos
string = "hola mundo"
print("Primer elemento", string[0]) 
print("Segundo elemento", string[1])
print("Ultimo elemento", string[-1])

# tambien podemos sacar porciones de una dacena
print(mix[0:2])
print(mix[:2])
print(mix[2:])
print(mix[2:-2])

# metodos estos para añadir o quitar
print(mix)
mix.append(False) # el metodo append es para agregar un elemento al final de la lista 
print(mix)
mix.append(["a","b"])
print(mix)

mix.insert(1,["a","b"]) # Aqui con insert agregaremos en la posicion 1
print(mix)

print(mix.index(["a","b"])) # con index es para saber en que posicion esta

numbers1 = [1,2,100.01,90.45,3,4,5] 
print(numbers1)
print("Mayor", max(numbers1)) # max es para imprimr el elemento mayor
print("Memor", min(numbers1)) # min es para imprimr el elemento menor
del numbers1[-1] # del usamos para eliminar elementos [escogemos que eleiminar]
print(numbers1)
del numbers1[:2]
print(numbers1)
del numbers1 # al no especifir eleiminamos todo la lista
print(numbers1)


