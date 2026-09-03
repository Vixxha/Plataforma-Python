# === METADATA ===
# title: Matriz Transpuesta
# description: Escribe una función que reciba una matriz (lista de listas) representada como un vector bidimensional de dimensiones $N \times M$ y devuelva su matriz transpuesta ($M \times N$). Las filas de la matriz original se convierten en las columnas de la matriz transpuesta.
# difficulty: Intermedio
# expected_output: [[1, 4], [2, 5], [3, 6]]
# hint: Puedes usar comprensión de listas anidadas iterando sobre los índices de las columnas y luego sobre las filas, o bien utilizar la función zip() junto con el operador de desempaquetado (*).

# === SOLUTION ===
def matriz_transpuesta(matriz):
    if not matriz or not matriz[0]:
        return []
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

# === TESTS ===
try:
    assert matriz_transpuesta([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]], "Error: el test 1 ha fallado."
    assert matriz_transpuesta([[1, 2], [3, 4]]) == [[1, 3], [2, 4]], "Error: considera casos límites en tu lógica."
    assert matriz_transpuesta([[5]]) == [[5]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")