# === METADATA ===
# title: Transponer y Filtrar Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros y devuelva una nueva matriz transpuesta (intercambiando filas por columnas), pero omitiendo aquellos números que sean negativos (reemplazándolos por 0). Asume que la matriz de entrada siempre es rectangular (todas las filas tienen la misma longitud).
# difficulty: Intermedio
# expected_output: [[1, 0, 5], [0, 4, 6]] para la entrada [[1, -2, 3], [-4, 4, 5], [5, 6, -1]]
# hint: Primero puedes construir la transpuesta iterando sobre los índices de columnas y filas, y luego aplicar la condición para limpiar los números negativos.

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
    assert transponer_y_filtrar([[1, -2, 3], [-4, 4, 5], [5, 6, -1]]) == [[1, 0, 5], [0, 4, 6], [3, 5, 0]], "Error: el test 1 ha fallado."
    assert transponer_y_filtrar([[-1, -1], [-2, -2]]) == [[0, 0], [0, 0]], "Error: considera casos límites en tu lógica."
    assert transponer_y_filtrar([[10, 20]]) == [[10], [20]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")