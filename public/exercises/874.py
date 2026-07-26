# === METADATA ===
# title: Filtrar y Multiplicar Números Pares
# description: Escribe una función que reciba una lista de números enteros, filtre únicamente los números pares, multiplique cada uno de ellos por 3 si son divisibles por 4, o por 2 en caso contrario, y devuelva la suma total de los valores resultantes.
# difficulty: Intermedio
# expected_output: 48
# hint: Utiliza un ciclo for para recorrer la lista y condicionales if/else para aplicar la lógica según el número sea par y divisible por 4.

# === SOLUTION ===
def procesar_pares(numeros):
    suma_total = 0
    for num in numeros:
        if num % 2 == 0:
            if num % 4 == 0:
                suma_total += num * 3
            else:
                suma_total += num * 2
    return suma_total

# === TESTS ===
try:
    assert procesar_pares([1, 2, 3, 4, 5, 6]) == 28, "Error: el test 1 ha fallado."
    assert procesar_pares([4, 8, 12]) == 72, "Error: considera casos límites en tu lógica."
    assert procesar_pares([1, 3, 5, 7]) == 0, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")