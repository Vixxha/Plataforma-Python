# === METADATA ===
# title: Filtrar y Multiplicar Números Pares
# description: Escribe una función que reciba una lista de números enteros, filtre únicamente los números pares, multiplique cada uno de ellos por 3 si son mayores que 4, o por 2 en caso contrario, y devuelva la suma total de los valores resultantes. Si la lista está vacía o no hay pares, debe devolver 0.
# difficulty: Intermedio
# expected_output: 34
# hint: Utiliza un bucle for o comprensión de listas para iterar sobre los elementos, y aplica estructuras condicionales (if-else) para evaluar cada número según las reglas dadas.

# === SOLUTION ===
def procesar_pares(numeros):
    suma_total = 0
    for num in numeros:
        if num % 2 == 0:
            if num > 4:
                suma_total += num * 3
            else:
                suma_total += num * 2
    return suma_total

# === TESTS ===
try:
    assert procesar_pares([1, 2, 3, 4, 5, 6]) == 34, "Error: el test 1 ha fallado."
    assert procesar_pares([2, 4]) == 16, "Error: considera casos límites en tu lógica."
    assert procesar_pares([]) == 0, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")