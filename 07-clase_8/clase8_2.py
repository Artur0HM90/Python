a =  [1,2,3,4,5]
b = a
print(a) # imprimimos a
print(b) # imprimimos a
del a[0] # eliminamos el elemento 0
print(a) # volvemos a imprimimos a
print(b) # volvemos a imprimimos b
print(id(a)) # el id con esto verificamos donde se guardo esa variable
print(id(b)) # el id con esto verificamos donde se guardo esa variable
# ya que las dos variables e guardan en el mismo espacio de memoria sale el mismo id
c=a[:] # creamos otra variable para guardar a
print(id(a)) # el id con esto verificamos donde se guardo esa variable
print(id(b)) # el id con esto verificamos donde se guardo esa variable
print(id(c)) # el id con esto verificamos donde se guardo esa variable
# cuando agregamos la variable c se guardo en otro espacio pero a,b tienen el mismo id
a.append(6) # aqui apregamos el elemeto a la lista a al final
print(a) # imprimimos a
print(b) # imprimimos b
print(c) # imprimimos c
# aqui vemos que a,b siguen imprimiendo lo mismo con lo que se agrego pero la variable c sigue igual con ele elemto borrado 

# esto se llama el slicing