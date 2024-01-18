numeros = [2,4,1,45,75,22]

#numeros.sort() # El metodo de sort() ordena la lista de números
#numeros.sort(reverse=True) # Caudno agregamos un argumento a sort(reverse=True) ordena la lista de forma desendente
numeros2 = sorted(numeros) # lo que sorted hizo fue devolver una lista ordena nueva no toca la original
numeros2 = sorted(numeros, reverse=True) # lo que sorted hizo fue devolver una lista de forma desendente nueva no toca la original
print(numeros)
print(numeros2)


usuario = [
    ["Arturo", 4], 
    ["Claudia", 1],
    ["Miguel", 5]]

def ordena(elemento):
    return elemento[1]
usuario.sort(key=ordena, reverse=True)
print(usuario)