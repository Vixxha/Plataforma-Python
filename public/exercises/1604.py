# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz (transpuesta) donde las filas se convierten en columnas, pero filtrando únicamente aquellos números que sean pares. Si una fila o columna resultante queda vacía tras el filtrado, debe incluirse como una lista vacía.
# difficulty: Intermedio
# expected_output: [[2, 4], [6], [8]]
# hint: Recuerda que para transponer una matriz puedes usar bucles anidados o la compresión de listas iterando sobre los índices de las columnas y filas originales.

# === SOLUTION ===
def transponer_y_filtrar_pares(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    transpuesta_filtrada = []
    
    for c in range(columnas):
        nueva_fila = []
        for f in range(filas):
            elemento = matriz[f][c]
            if elemento % 2 == 0:
                nueva_fila.append(elemento)
        transpuesta_filtrada.append(nueva_fila)
        
    return transpuesta_filtrada

# === TESTS ===
try:
    assert transponer_y_filtrar_pares([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]][1::2], "Error: el test 1 ha fallado."
    assert transponer_y_filtrar_pares([[1, 3], [5, 7]]) == [[], []], "Error: considera casos límites en tu lógica."
    assert transponer_y_filtrar_pares([[2, 3], [4, 6], [8, 9]]) == [[2, 4, 8], [6]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")