# === METADATA ===
# title: Filtrar y Multiplicar Vectores
# description: Escribe una función que reciba una lista de números enteros y un número escalar. La función debe retornar una nueva lista que contenga únicamente los números pares del vector original, pero multiplicados por el valor del escalar.
# difficulty: Intermedio
# expected_output: [4, 12, 16] para la entrada ([1, 2, 3, 4, 6, 9], 2)
# hint: Puedes usar una comprensión de lista (list comprehension) para filtrar los números pares con la condición `x % 2 == 0` y simultáneamente multiplicarlos por el escalar.

# === SOLUTION ===
def procesar_vector(vector, escalar):
    return [x * escalar for x in vector if x % 2 == 0]

# === TESTS ===
try:
    assert procesar_vector([1, 2, 3, 4, 6, 9], 2) == [4, 8, 12], "Error: el test 1 ha fallado."
    assert procesar_vector([5, 7, 9], 3) == [], "Error: considera casos límites en tu lógica donde no hay números pares."
    assert procesar_vector([2, 4, 6], 5) == [10, 20, 30], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")