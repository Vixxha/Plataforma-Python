# === METADATA ===
# title: Filtro de Matrices Cuadradas
# description: Crea una función que reciba una matriz cuadrada (lista de listas) y devuelva una nueva lista conteniendo solo los elementos situados en la diagonal principal (donde el índice de fila es igual al de columna).
# difficulty: Intermedio
# expected_output: Para [[1, 2], [3, 4]], retorna [1, 4]
# hint: Puedes usar un solo bucle for e indexar la fila y la columna con la misma variable.

# === SOLUTION ===
def extraer_diagonal(matriz):
    resultado = []
    for i in range(len(matriz)):
        resultado.append(matriz[i][i])
    return resultado

# === TESTS ===
try:
    assert extraer_diagonal([[1, 2], [3, 4]]) == [1, 4], "Error: el test 1 ha fallado."
    assert extraer_diagonal([[10, 0, 0], [0, 20, 0], [0, 0, 30]]) == [10, 20, 30], "Error: considera casos límites en tu lógica."
    assert extraer_diagonal([[5]]) == [5], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")