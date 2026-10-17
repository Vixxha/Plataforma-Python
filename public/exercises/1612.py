# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz donde se hayan eliminado aquellas filas cuya suma de elementos sea un número impar. Además, la matriz resultante debe estar transpuesta (intercambiar filas por columnas).
# difficulty: Intermedio
# expected_output: [[1, 3], [2, 4]]
# hint: Primero filtra las filas cuya suma sea par (suma % 2 == 0). Luego, recuerda que para transponer una matriz puedes usar list comprehensions combinadas con zip(*matriz).

# === SOLUTION ===
def transponer_y_filtrar_matriz(matriz):
    if not matriz:
        return []
    
    # Filtrar filas cuya suma sea par
    filas_filtradas = [fila for fila in matriz if sum(fila) % 2 == 0]
    
    if not filas_filtradas:
        return []
    
    # Transponer la matriz resultante
    matriz_transpuesta = [list(columna) for columna in zip(*filas_filtradas)]
    
    return matriz_transpuesta

# === TESTS ===
try:
    assert transponer_y_filtrar_matriz([[1, 2], [3, 4]]) == [[1, 3], [2, 4]], "Error: el test 1 ha fallado."
    assert transponer_y_filtrar_matriz([[1, 1], [2, 2], [3, 3]]) == [[2], [2]], "Error: considera casos límites en tu lógica."
    assert transponer_y_filtrar_matriz([[1, 3], [5, 7]]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")