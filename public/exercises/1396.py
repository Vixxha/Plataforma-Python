# === METADATA ===
# title: Matriz Transpuesta e Intercambio
# description: Escribe una función que reciba una matriz cuadrada (representada como una lista de listas) y devuelva su matriz transpuesta (intercambiar filas por columnas). Además, como requisito adicional de transformación, multiplica por 2 todos los elementos de la diagonal principal.
# difficulty: Intermedio
# expected_output: [[2, 3], [4, 8]]
# hint: Puedes recorrer la matriz usando índices o comprensiones de lista, y verificar si el índice de la fila es igual al de la columna para aplicar la multiplicación por 2.

# === SOLUTION ===
def transponer_y_duplicar_diagonal(matriz):
    n = len(matriz)
    transpuesta = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            valor = matriz[j][i]
            if i == j:
                valor *= 2
            transpuesta[i][j] = valor
    return transpuesta

# === TESTS ===
try:
    assert transponer_y_duplicar_diagonal([[1, 2], [3, 4]]) == [[2, 3], [4, 8]], "Error: el test 1 ha fallado."
    assert transponer_y_duplicar_diagonal([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == [[2, 0, 0], [0, 2, 0], [0, 0, 2]], "Error: considera casos límites en tu lógica."
    assert transponer_y_duplicar_diagonal([[5]]) == [[10]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")