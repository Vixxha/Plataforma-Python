# === METADATA ===
# title: Filtro de Matrices Cuadradas
# description: Crea una función que reciba una matriz cuadrada (lista de listas) de números enteros y devuelva una nueva lista que contenga únicamente los elementos de la diagonal principal (donde el índice de fila es igual al índice de columna) ordenados de forma ascendente.
# difficulty: Intermedio
# expected_output: [1, 5, 9] para una matriz de 3x3 con diagonal [5, 1, 9]
# hint: La diagonal principal de una matriz se accede cuando el índice i es igual al índice j (matriz[i][i]). Recuerda usar un método de ordenamiento después de extraer los elementos.

# === SOLUTION ===
def filtrar_diagonal_ordenada(matriz):
    diagonal = []
    for i in range(len(matriz)):
        diagonal.append(matriz[i][i])
    diagonal.sort()
    return diagonal

# === TESTS ===
try:
    assert filtrar_diagonal_ordenada([[5, 2, 3], [4, 1, 6], [7, 8, 9]]) == [1, 5, 9], "Error: el test 1 ha fallado."
    assert filtrar_diagonal_ordenada([[10, 0], [0, 5]]) == [5, 10], "Error: considera casos límites en tu lógica."
    assert filtrar_diagonal_ordenada([[1]]) == [1], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")