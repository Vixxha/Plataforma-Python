# === METADATA ===
# title: Operaciones Básicas en Matrices
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva una lista con la suma de los elementos de cada fila. Si la matriz está vacía, debe retornar una lista vacía.
# difficulty: Intermedio
# expected_output: [6, 15, 24]
# hint: Puedes iterar sobre cada fila de la matriz y utilizar la función integrada sum() para calcular el total de cada fila.

# === SOLUTION ===
def sumar_filas_matriz(matriz):
    if not matriz:
        return []
    return [sum(fila) for fila in matriz]

# === TESTS ===
try:
    assert sumar_filas_matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [6, 15, 24], "Error: el test 1 ha fallado."
    assert sumar_filas_matriz([[-1, 1], [0, 0], [10, -5]]) == [0, 0, 5], "Error: considera casos límites en tu lógica."
    assert sumar_filas_matriz([]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")