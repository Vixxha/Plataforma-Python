# === METADATA ===
# title: Transponer y Sumar Diagonales de una Matriz Cuadrada
# description: Escribe una función que reciba una matriz cuadrada (representada como una lista de listas) y devuelva una tupla con dos elementos: primero, la matriz transpuesta, y segundo, la suma de los elementos de su diagonal principal.
# difficulty: Intermedio
# expected_output: ([[1, 4], [2, 5]], 6)
# hint: Puedes usar listas por comprensión para construir la matriz transpuesta y recorrer la diagonal principal utilizando índices que coincidan en fila y columna (i == j).

# === SOLUTION ===
def procesar_matriz(matriz):
    n = len(matriz)
    transpuesta = [[matriz[j][i] for j in range(n)] for i in range(n)]
    suma_diagonal = sum(matriz[i][i] for i in range(n))
    return (transpuesta, suma_diagonal)

# === TESTS ===
try:
    assert procesar_matriz([[1, 2], [3, 4]]) == ([[1, 3], [2, 4]], 5), "Error: el test 1 ha fallado."
    assert procesar_matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == ([[1, 4, 7], [2, 5, 8], [3, 6, 9]], 15), "Error: considera casos límites en tu lógica."
    assert procesar_matriz([[5]]) == ([[5]], 5), "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")