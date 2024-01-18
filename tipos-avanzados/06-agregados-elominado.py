mascotas = ["Dino","Pelusa", "Pulga", "Felipe", "Pulga", "Chanchito feliz"]

mascotas.insert(1,"Melvin") # La sintaxis insert agregamos un elemento a la lista
mascotas.append("Drogui") # La sintaxis append agregamos un elemento al final

mascotas.remove("Pulga") # La sintaxis remove remuene un elemento si hay mas de un duplicado no va funcionar
mascotas.pop() # La sintaxis pop elimina el elemto final.
mascotas.pop(1) # La sintaxis pop elimina el elemento señalado
del mascotas[0] # usando la palabra recervado del. ahi debemos señalar el indice que se va eliminar.
mascotas.clear()
print(mascotas)