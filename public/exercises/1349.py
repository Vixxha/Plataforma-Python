# === METADATA ===
# title: Transponer y Promediar una Matriz
# description: Escribe una función que reciba una matriz (lista de listas) de números enteros o flotantes de tamaño N x M. La función debe retornar una nueva matriz (lista de listas) que sea la transpuesta de la original (intercambiando filas por columnas).
# difficulty: Intermedio
# expected_output: [[1, 4], [2, 5], [3, 6]]
# hint: Puedes usar list comprehensions o bucles anidados recorriendo los índices de las columnas y luego de las filas.

# === SOLUTION ===
def transponer_matriz(matriz):
    if not matriz or not matriz[0]:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    matriz_transpuesta = []
    for c in range(columnas):
        nueva_fila = []
        for f in range(filas):
            nueva_fila.append(matriz[f][c])
        matriz_transpuesta.append(nueva_fila)
        
    return matriz_transpuesta

# === TESTS ===
try:
    assert transponer_matriz([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]], "Error: el test 1 ha fallado."
    assert transponer_matriz([[1]]) == [[1]], "Error: considera casos límites en tu lógica."
    assert transponer_matriz([[1, 2], [3, 4], [5, 6]]) == [[1, 3, 5], [2, 4, 6]], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")