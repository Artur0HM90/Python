datos = {"Nombre":"Arturo", "Edad":34,"Ocupación":"Estudiante"}
print(datos)
agragarClave = str(input("Ingresa un clave: ").capitalize())
agragarValor = str(input("Ingresa un valor: ").capitalize())
datos.update({agragarClave: agragarValor}) # update es para agregar datos a una biblioteca
print(datos)