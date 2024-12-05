# Estas son las 3 formas de usar comillas
name = "Arturo"
name2 = 'Miguel'
name3 = '''Hurtado Méndez'''

nombres = "ARTURO Miguel"
apellidos = "Hurtado Méndez"
print(type(name)) # usamos Type para saber que tipo de variable es.
print(name2)
print(name3)

print(name[0]) # usamos los corchetes para elegir el número de caracer.
print(name[1])
print
(name[2])
    #print(name[20]) # Hay que tener cuidado en salirnos del margen de nuestra cadena.

# Si queremos contar desde el final al inicio hacemos los siguiente
print(name[-1])
print(name[-2])

# Con las cademos podemos hacer 2 cosas importantes 1. la concatenación (es Cuando juntamos dos cadenas) 2. la repetición cuando le decimos que deseamos multiplicar o repetir ciertas veces esta cadena

print(nombres * 5)

print(nombres + " " + apellidos)

# Tambien hay acciones que podemos hacer con las cadenas una de ellas es consultar la longitud de caracteres que exiasten
print(len(nombres))  # len usamos para saber la longitud de nuestra cadena
print(len(apellidos))

# Pero hay funciones propias de este tipo de datos que es el STRING que se llaman metodos hay que tener cuidado ya que una sintaxis diferente a las funciones.

print(nombres.lower()) # El metodo LOWER funciona para que el string este en minuscaula.
print(nombres.upper()) # El metodo UPPER funciona para que el string este en mayuscula.
print(apellidos.strip()) # El metodo STRIP funciona para que el string este elimine todos los espacios.