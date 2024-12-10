# los diccionarios en python son una estructura que almacena 2 datos (1. la clave) (2. el valor) se pueden ver su uso en la vida diaria cuando buscamos en un diccionario una palabra -> la palabra seria la clave y el concepto seria el valor.

numbers = {1:"uno", 2:"dos", 3:"tres"}
print(numbers)
print(numbers[2])

information = {"Nombres": "Arturo Miguel",
            "Apellidos":"Hurtaso Méndez",
            "Altura":"1.74",
            "Edad":34}
print (information)   
del information ["Edad"]
print (information)   

# metodo keys

claves = information.keys()
print (claves)
print (type(claves))

# metodo values

values = information.values()
print(values)

# metodo  items (es para llamar a los pares)
pairs = information.items()
print(pairs)

contact = {"Arturo":{"Apellidos":"Hurtado Méndez",
        "Altura":"1.74",
        "Edad":34},
        "Luis":{"Apellidos":"Masa",
        "Altura":"1.94",
        "Edad":24}}
print(contact)
print(contact["Arturo"])