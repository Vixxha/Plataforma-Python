# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz transpuesta (intercambiando filas por columnas), pero omitiendo aquellos valores que sean números negativos. En su lugar, los números negativos deben ser reemplazados por un 0.
# difficulty: Intermedio
# expected_output: [[1, 0, 5], [0, 4, 6]] para la entrada [[1, -2], [3, 4], [-5, 6]]
# hint: Puedes recorrer la matriz original usando sus índices (filas y columnas) o utilizar la comprensión de listas para construir la matriz transpuesta fila por fila.

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
            val = matriz[f][c]
            nueva_fila.append(val if val >= 0 else 0)
        resultado.append(nueva_fila)
        
    return resultado

# === TESTS ===
try:
    assert transponer_y_filtrar([[1, -2], [3, 4], [-5, 6]]) == [[1, 0, 5], [0, 4, 6]], "Error: el test 1 ha fallado."
    assert transponer_y_filtrar([[-1, -1], [-1, -1]]) == [[0, 0], [0, 0]], "Error: considera casos límites en tu lógica."
    assert transponer_y_filtrar([[10, 20]]) == [[10], [20]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")