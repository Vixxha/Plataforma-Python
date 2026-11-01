# === METADATA ===
# title: Filtrar y Multiplicar Vectores
# description: Escribe una función que reciba una lista de números enteros y un número entero multiplicador. La función debe retornar una nueva lista que contenga únicamente los números pares del vector original, pero multiplicados por el valor dado.
# difficulty: Intermedio
# expected_output: [4, 12] para la entrada ([1, 2, 3, 4, 5], 2)
# hint: Puedes utilizar una comprensión de listas para filtrar los elementos pares (numero % 2 == 0) y multiplicarlos simultáneamente.

# === SOLUTION ===
def filtrar_y_multiplicar(vector, multiplicador):
    return [num * multiplicador for num in vector if num % 2 == 0]

# === TESTS ===
try:
    assert filtrar_y_multiplicar([1, 2, 3, 4, 5], 2) == [4, 8], "Error: el test 1 ha fallado."
    assert filtrar_y_multiplicar([10, 15, 20, 25], 3) == [30, 60], "Error: considera casos límites en tu lógica."
    assert filtrar_y_multiplicar([1, 3, 5, 7], 5) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")