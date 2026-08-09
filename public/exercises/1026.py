# === METADATA ===
# title: Filtrar y Trasponer Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros. La función debe eliminar todas las filas donde la suma de sus elementos sea un número par, y posteriormente devolver la matriz resultante traspuesta (intercambiando filas por columnas). Si la matriz resultante queda vacía, debe retornar una lista vacía.
# difficulty: Intermedio
# expected_output: [[1, 4], [2, 5], [3, 6]]
# hint: Primero calcula la suma de cada fila para filtrar cuáles mantener. Luego, puedes usar listas por comprensión o bucles anidados para construir la matriz traspuesta.

# === SOLUTION ===
def filtrar_y_trasponer(matriz):
    if not matriz:
        return []
    
    # Filtrar filas cuya suma sea impar
    filas_filtradas = [fila for fila in matriz if sum(fila) % 2 != 0]
    
    if not filas_filtradas:
        return []
    
    # Trasponer la matriz resultante
    filas = len(filas_filtradas)
    columnas = len(filas_filtradas[0])
    
    matriz_transpuesta = []
    for c in range(columnas):
        nueva_fila = [filas_filtradas[f][c] for f in range(filas)]
        matriz_transpuesta.append(nueva_fila)
        
    return matriz_transpuesta

# === TESTS ===
try:
    assert filtrar_y_trasponer([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]], "Error: el test 1 ha fallado."
    assert filtrar_y_trasponer([[2, 4], [6, 8]]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_y_trasponer([[1, 1], [2, 2], [3, 1]]) == [[1, 3], [1, 1]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")