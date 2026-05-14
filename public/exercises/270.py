# === METADATA ===
# title: Filtro de Matrices Cuadradas
# description: Crea una función que reciba una matriz cuadrada (lista de listas) y devuelva una lista unidimensional con todos los elementos que se encuentren en la diagonal principal (donde el índice de fila es igual al de columna).
# difficulty: Intermedio
# expected_output: [1, 5, 9] para una matriz [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# hint: Utiliza un único ciclo for para iterar sobre los índices i y accede a la posición [i][i] de la matriz.

# === SOLUTION ===
def obtener_diagonal(matriz):
    diagonal = []
    for i in range(len(matriz)):
        diagonal.append(matriz[i][i])
    return diagonal

# === TESTS ===
try:
    assert obtener_diagonal([[1, 2], [3, 4]]) == [1, 4], "Error: el test 1 ha fallado."
    assert obtener_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 5, 9], "Error: considera casos límites en tu lógica."
    assert obtener_diagonal([[10]]) == [10], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")