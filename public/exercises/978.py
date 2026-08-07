# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz transpuesta (intercambiando filas por columnas), pero omitiendo aquellos valores que sean múltiplos de 3.
# difficulty: Intermedio
# expected_output: [[1, 4], [2, 5]]
# hint: Puedes recorrer la matriz original usando índices o utilizando una comprensión de listas avanzada para construir las nuevas filas y columnas, aplicando un condicional para filtrar.

# === SOLUTION ===
def transponer_y_filtrar(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    transpuesta_filtrada = []
    
    for c in range(columnas):
        nueva_fila = []
        for f in range(filas):
            valor = matriz[f][c]
            if valor % 3 != 0:
                nueva_fila.append(valor)
        transpuesta_filtrada.append(nueva_fila)
        
    return transpuesta_filtrada

# === TESTS ===
try:
    assert transponer_y_filtrar([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], []], "Error: el test 1 ha fallado."
    assert transponer_y_filtrar([[3, 6], [9, 12]]) == [[], []], "Error: considera casos límites en tu lógica."
    assert transponer_y_filtrar([[1, 2], [3, 4], [5, 6]]) == [[1, 5], [2, 4]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")