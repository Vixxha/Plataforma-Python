# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz transpuesta (intercambiando filas por columnas), pero omitiendo aquellos números que sean negativos.
# difficulty: Intermedio
# expected_output: [[1, 4], [2, 5]]
# hint: Recuerda que la transposición de una matriz implica recorrer las columnas originales para convertirlas en filas de la nueva matriz. Puedes usar comprensión de listas.

# === SOLUTION ===
def transponer_y_filtrar(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    resultado = []
    
    for c in range(columnas):
        nueva_fila = []
        for f in range(filas):
            valor = matriz[f][c]
            if valor >= 0:
                nueva_fila.append(valor)
        resultado.append(nueva_fila)
        
    return resultado

# === TESTS ===
try:
    assert transponer_y_filtrar([[1, -2, 3], [4, 5, -6]]) == [[1, 4], [], [3]], "Error: el test 1 ha fallado."
    assert transponer_y_filtrar([[1, 2], [3, 4]]) == [[1, 3], [2, 4]], "Error: considera casos límites en tu lógica."
    assert transponer_y_filtrar([[-1, -2], [-3, -4]]) == [[], []], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")