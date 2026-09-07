# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz transpuesta (intercambiando filas por columnas), pero donde solo se incluyan aquellas columnas cuya suma total sea un número par. Si ninguna columna cumple esta condición, debe retornar una lista vacía.
# difficulty: Intermedio
# expected_output: [[2, 4], [6, 8]]
# hint: Primero calcula la transpuesta de la matriz original iterando sobre los índices de columnas y filas. Luego, evalúa la suma de cada nueva fila (columna original) antes de añadirla al resultado final.

# === SOLUTION ===
def transponer_y_filtrar(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    transpuesta_filtrada = []
    
    for c in range(columnas):
        columna_actual = [matriz[f][c] for f in range(filas)]
        if sum(columna_actual) % 2 == 0:
            transpuesta_filtrada.append(columna_actual)
            
    return transpuesta_filtrada

# === TESTS ===
try:
    assert transponer_y_filtrar([[1, 2], [3, 4]]) == [[1, 3], [2, 4]], "Error: el test 1 ha fallado."
    assert transponer_y_filtrar([[1, 1], [1, 1]]) == [], "Error: considera casos límites en tu lógica."
    assert transponer_y_filtrar([[2, 3], [4, 5]]) == [[2, 4]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")