# === METADATA ===
# title: Transponer Matriz 3x3
# description: Escribe una función que reciba una matriz (lista de listas) de 3x3 y devuelva su matriz transpuesta (intercambiando filas por columnas).
# difficulty: Intermedio
# expected_output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
# hint: Puedes usar comprensión de listas para acceder a los elementos por índice de columna: matriz[j][i].

# === SOLUTION ===
def transponer_matriz(matriz):
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

# === TESTS ===
try:
    assert transponer_matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]], "Error: el test 1 ha fallado."
    assert transponer_matriz([[0, 1], [2, 3], [4, 5]]) == [[0, 2, 4], [1, 3, 5]], "Error: considera casos límites en tu lógica."
    assert transponer_matriz([[5]]) == [[5]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")