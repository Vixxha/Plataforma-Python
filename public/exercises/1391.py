# === METADATA ===
# title: Transponer Matriz Cuadrada
# description: Escribe una función que reciba una matriz cuadrada (representada como una lista de listas) y devuelva su transpuesta (intercambiando filas por columnas).
# difficulty: Intermedio
# expected_output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
# hint: Puedes recorrer la matriz original usando índices [i][j] y asignar esos valores a la posición [j][i] en una nueva matriz.

# === SOLUTION ===
def transponer_matriz(matriz):
    n = len(matriz)
    # Crear una nueva matriz de n x n inicializada en ceros
    transpuesta = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            transpuesta[j][i] = matriz[i][j]
    return transpuesta

# === TESTS ===
try:
    assert transponer_matriz([[1, 2], [3, 4]]) == [[1, 3], [2, 4]], "Error: el test 1 ha fallado."
    assert transponer_matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]], "Error: considera casos límites en tu lógica."
    assert transponer_matriz([[5]]) == [[5]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")