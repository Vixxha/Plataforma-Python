# === METADATA ===
# title: Transponer Matriz Cuadrada
# description: Escribe una función que reciba una matriz cuadrada (representada como una lista de listas) y devuelva su transpuesta. La transpuesta de una matriz se obtiene intercambiando sus filas por columnas.
# difficulty: Intermedio
# expected_output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
# hint: Puedes usar comprensión de listas anidadas iterando sobre los índices de las columnas y filas.

# === SOLUTION ===
def transponer_matriz(matriz):
    if not matriz:
        return []
    filas = len(matriz)
    columnas = len(matriz[0])
    return [[matriz[j][i] for j in range(filas)] for i in range(columnas)]

# === TESTS ===
try:
    assert transponer_matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]], "Error: el test 1 ha fallado."
    assert transponer_matriz([[1, 2], [3, 4]]) == [[1, 3], [2, 4]], "Error: considera casos límites en tu lógica."
    assert transponer_matriz([[5]]) == [[5]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")