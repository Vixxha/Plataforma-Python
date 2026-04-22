# === METADATA ===
# title: Matriz de Simetría Inversa
# description: Crea una función que reciba una matriz cuadrada (lista de listas) de números enteros y devuelva una nueva matriz donde cada fila sea la inversa de la original (orden invertido de elementos).
# difficulty: Intermedio
# expected_output: [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
# hint: Puedes usar el slicing de Python [::-1] para invertir cada lista interna dentro de una comprensión de listas.

# === SOLUTION ===
def invertir_filas_matriz(matriz):
    return [fila[::-1] for fila in matriz]

# === TESTS ===
try:
    assert invertir_filas_matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[3, 2, 1], [6, 5, 4], [9, 8, 7]], "Error: el test 1 ha fallado."
    assert invertir_filas_matriz([[10, 20], [30, 40]]) == [[20, 10], [40, 30]], "Error: considera casos límites en tu lógica."
    assert invertir_filas_matriz([[1]]) == [[1]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")