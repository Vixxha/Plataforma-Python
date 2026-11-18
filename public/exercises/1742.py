# === METADATA ===
# title: Operaciones Básicas en Matrices: Suma por Filas
# description: Escribe una función que reciba una matriz (lista de listas de números) de tamaño n x m y retorne una lista de una sola dimensión (vector) donde cada elemento sea la suma de los valores de su respectiva fila.
# difficulty: Intermedio
# expected_output: [15, 9, 24]
# hint: Puedes iterar sobre cada fila de la matriz y usar la función incorporada sum() para calcular la suma de sus elementos.

# === SOLUTION ===
def suma_filas(matriz):
    return [sum(fila) for fila in matriz]

# === TESTS ===
try:
    assert suma_filas([[1, 2, 3], [4, 5], [6, 7, 8, 3]]) == [6, 9, 24], "Error: el test 1 ha fallado."
    assert suma_filas([[10, -2, 5], [0, 0, 0], [-5, 5]]) == [13, 0, 0], "Error: considera casos límites en tu lógica."
    assert suma_filas([]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")