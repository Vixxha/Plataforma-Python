# === METADATA ===
# title: Filtrado de Matriz y Suma Diagonal
# description: Dada una matriz cuadrada (lista de listas) de números enteros, devuelve una nueva lista que contenga los elementos de la diagonal principal. Si la suma de estos elementos es par, devuelve la lista; si es impar, devuelve la lista invertida.
# difficulty: Intermedio
# expected_output: [1, 5, 9] (si la suma es par) o [9, 5, 1] (si la suma es impar)
# hint: La diagonal principal de una matriz cuadrada ocurre cuando el índice de la fila es igual al índice de la columna (i == j).

# === SOLUTION ===
def procesar_diagonal(matriz):
    n = len(matriz)
    diagonal = [matriz[i][i] for i in range(n)]
    
    if sum(diagonal) % 2 == 0:
        return diagonal
    else:
        return diagonal[::-1]

# === TESTS ===
try:
    assert procesar_diagonal([[1, 2], [3, 4]]) == [4, 1], "Error: La suma 5 es impar, debió invertir la diagonal [1, 4]."
    assert procesar_diagonal([[1, 0, 0], [0, 2, 0], [0, 0, 1]]) == [1, 2, 1], "Error: La suma 4 es par, debió mantener el orden [1, 2, 1]."
    assert procesar_diagonal([[10]]) == [10], "Error: El caso de matriz 1x1 falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")