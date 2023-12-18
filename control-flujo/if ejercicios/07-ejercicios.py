"""
Categorizar edad:
Solicitar al usuario que ingrese su edad e imprimir en qué categoría se encuentra: 
niño (0-12 años), 
adolescente (13-19 años), 
adulto (20-64 años) o 
adulto mayor (65 años en adelante).
"""

categoria_edad = int(input("Ingresa edad: "))

if categoria_edad <= 0 or categoria_edad <= 12:
    print(f"Tu edad es {categoria_edad} eres un niño.")

elif categoria_edad <= 13 or categoria_edad <= 19:
    print (f"Tu edad es {categoria_edad} eres un adolescente.")

elif categoria_edad <= 20 or categoria_edad <= 64:
    print(f"Tu edad es {categoria_edad} eres un adulto.")

else:
    print(f"Tu edad es {categoria_edad} eres un adulto mayor.")