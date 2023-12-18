"""Calificación de un estudiante:
Pedir al usuario que ingrese 4 calificación. Si la calificación es mayor o igual a 
0 - 5   Reprobado
6 - 10  Sustitutorio
11 - 15 Aprobado
16 - 20 Excelente 
"""

print ("Ingresa las notas de alumno.")

primera_nota = int(input("Ingresa la primera nota: "))
segunda_nota = int(input("Ingresa la segunda nota: "))
tercera_nota = int(input("Ingresa la tercera nota: "))
cuarta_nota = int(input("Ingresa la cuarta nota: "))

nota_final = ((primera_nota + segunda_nota + tercera_nota + cuarta_nota) / 4)

if nota_final < 0 or nota_final <= 5:
    print(f"La nota final es: {nota_final} esta reprabado")

elif nota_final <=6 or nota_final <= 10:
    print(f"La nota final es: {nota_final} tiene derecho a sustitutorio.")

elif nota_final <= 11 or nota_final <= 15:
    print(f"La nota final es: {nota_final} esta aprobado.")

else:
    print(f"La nota final es: {nota_final} es un alumno excelente.")