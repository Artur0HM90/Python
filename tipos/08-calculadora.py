n1 = input("Ingresa primer número: ")
n2 = input("Ingresa segundo número: ")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
divi = n1 / n2

mensaje = f"""
Para los números {n1} y {n2},
el serultado de la suma es {suma}
el serultado de la resta es {resta}
el serultado de la multiplicacion es {multi}
el serultado de la division es {divi}"""

print(mensaje)
