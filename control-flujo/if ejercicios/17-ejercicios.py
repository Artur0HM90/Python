"""
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
"""

print("""Bienvenico a la Pizseria Bella que pizza quieres:
1: Vegetariana.
2: No vegetariana.
""")

primer_ingredientes_vegetarianos = "Pimienta"
segundo_ingredientes_vegetarianos = "Tofu"
primer_ingredientes_no_vegetarianos = "Peperoni"
segundo_ingredientes_no_vegetarianos = "Jamón"
tercer_ingredientes_no_vegetarianos = "Salmón"

pizza = int(input("Que pizza vas a desear: "))

if pizza == 1:
    print("Elegiste la pizza vegetariana.")
    ingrediente_vegetarianos = str(input("Tienes opción de elegir ingredientes adicionales, deseas ingredientes adicionales SI - NO: "))

    if ingrediente_vegetarianos == "si" or ingrediente_vegetarianos == "SI" or ingrediente_vegetarianos == "S" or ingrediente_vegetarianos == "s":
        print(f"""Elegiste ingredientes adicionales. que deseas agregar:
1. {primer_ingredientes_vegetarianos}.
2. {segundo_ingredientes_vegetarianos}.
3. Desea los dos ingredientes.""")
