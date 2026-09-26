# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz donde se hayan eliminado aquellas filas cuya suma de elementos sea un número impar. Además, la matriz resultante debe estar transpuesta (las filas se convierten en columnas).
# difficulty: Intermedio
# expected_output: [[2, 4], [2, 6]]
# hint: Primero filtra las filas cuya suma sea par (usando `% 2 == 0`), y luego calcula la transpuesta utilizando comprensión de listas con índices `[row[i] for row in matriz_filtrada]`.

# === SOLUTION ===
def transponer_y_filtrar(matriz):
    if not matriz or not matriz[0]:
        return []
    
    # Filtrar filas cuya suma es par
    filas_pares = [fila for fila in matriz if sum(fila) % 2 == 0]
    
    if not filas_pares:
        return []
    
    # Transponer la matriz filtrada
    filas = len(filas_pares)
    columnas = len(filas_pares[0])
    
    matriz_transpuesta = [[filas_pares[r][c] for r in range(filas)] for c in range(columnas)]
    return matriz_transpuesta

# === TESTS ===
try:
    assert transponer_y_filtrar([[1, 2], [3, 4]]) == [[4], [6]], "Error: el test 1 ha fallado."
    assert transponer_y_filtrar([[1, 1], [2, 2], [3, 3]]) == [[2], [2]], "Error: considera casos límites en tu lógica."
    assert transponer_y_filtrar([[1, 3], [5, 7]]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")